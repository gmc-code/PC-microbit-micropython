import html
import hashlib
from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives, DirectiveError
from sphinx.util.docutils import SphinxDirective

# ─────────────────────────────────────
# Nodes
# ─────────────────────────────────────
class multichoice_node(nodes.General, nodes.Element):
    pass

class choice_container_node(nodes.General, nodes.Element):
    pass

class choice_label_node(nodes.General, nodes.Element):
    pass

# ─────────────────────────────────────
# HTML Visitors
# ─────────────────────────────────────
def visit_multichoice_html(self, node):
    shuffle_attr = str(node.get("shuffle", False)).lower()
    letters_attr = str(node.get("letters", False)).lower()
    single_attr = str(node.get("single_correct", False)).lower()
    theme_attr = node.get("theme", "light")

    self.body.append(
        f'<div class="multichoice-block theme-{theme_attr}" '
        f'data-multichoice-single="{single_attr}" '
        f'data-multichoice-shuffle="{shuffle_attr}" '
        f'data-multichoice-letters="{letters_attr}">'
    )

def depart_multichoice_html(self, node):
    self.body.append("</div>")

def visit_choice_container_html(self, node):
    is_correct = str(node.get("correct", False)).lower()
    self.body.append(f'<div class="multichoice-choice" data-correct="{is_correct}">')

def depart_choice_container_html(self, node):
    self.body.append("</div>")

def visit_choice_label_html(self, node):
    input_type = node.get("input_type", "radio")
    group_name = node.get("group_name", "")

    self.body.append('<label>')
    self.body.append(f'<input type="{input_type}" name="multichoice-{group_name}">')
    self.body.append('<span class="multichoice-letter"></span>')
    self.body.append('<div class="multichoice-choice-label">')

def depart_choice_label_html(self, node):
    self.body.append('</div>')
    self.body.append('</label>')

# ─────────────────────────────────────
# Directive
# ─────────────────────────────────────
class multichoiceDirective(SphinxDirective):
    has_content = True

    option_spec = {
        "no-shuffle": directives.flag,
        "no-letters": directives.flag,
        "theme": lambda argument: directives.choice(argument, ("light", "dark")),
    }

    def run(self):
        node = multichoice_node()

        # Core configuration options
        node["shuffle"] = "no-shuffle" not in self.options
        node["letters"] = "no-letters" not in self.options
        node["theme"] = self.options.get("theme", "light")

        # ─────────────────────────────────────
        # Separate Question Block from Choice Block
        # ─────────────────────────────────────
        choice_start_idx = None

        for idx, line in enumerate(self.content):
            stripped = line.strip()
            if stripped.startswith("[") and "]" in stripped:
                choice_start_idx = idx
                break

        if choice_start_idx is None:
            raise DirectiveError(3, "MCQ error: Missing answer choices block.")

        question_lines = self.content[:choice_start_idx]
        choice_lines = self.content[choice_start_idx:]

        # ─────────────────────────────────────
        # Parse the Question Natively
        # ─────────────────────────────────────
        question_container = nodes.container(classes=["multichoice-question"])
        self.state.nested_parse(question_lines, self.content_offset, question_container)
        node += question_container

        # ─────────────────────────────────────
        # Multi-line Choice Parser
        # ─────────────────────────────────────
        raw_choices = []
        current_choice = None

        for line_idx, line in enumerate(choice_lines):
            stripped = line.strip()

            if stripped.startswith("[") and "]" in stripped:
                marker = stripped[1].lower()
                is_correct = marker == "x"

                right_bracket_idx = line.find("]")
                content_start = line[right_bracket_idx + 1:]

                current_choice = {
                    "correct": is_correct,
                    "text_lines": [],
                    "explanation_lines": [],
                    "in_explanation": False
                }
                raw_choices.append(current_choice)

                if "|" in content_start:
                    txt, exp = content_start.split("|", 1)
                    if txt.strip():
                        current_choice["text_lines"].append(txt)
                    if exp.strip():
                        current_choice["explanation_lines"].append(exp)
                    current_choice["in_explanation"] = True
                else:
                    if content_start.strip():
                        current_choice["text_lines"].append(content_start)

            elif current_choice is not None:
                if "|" in line:
                    txt, exp = line.split("|", 1)
                    if txt.strip():
                        current_choice["text_lines"].append(txt)
                    if exp.strip():
                        current_choice["explanation_lines"].append(exp)
                    current_choice["in_explanation"] = True
                else:
                    if current_choice["in_explanation"]:
                        current_choice["explanation_lines"].append(line)
                    else:
                        current_choice["text_lines"].append(line)

        if not raw_choices:
            raise DirectiveError(3, "MCQ error: Missing answer choices block.")

        correct_count = sum(c["correct"] for c in raw_choices)
        if correct_count == 0:
            raise DirectiveError(3, "MCQ error: Must mark at least one option correct [x].")

        is_multi = correct_count > 1
        node["single_correct"] = not is_multi
        input_type = "checkbox" if is_multi else "radio"

        # Create a stable unique name based on option texts
        seed_string = "".join("".join(c["text_lines"]) for c in raw_choices)
        group_name = hashlib.md5(seed_string.encode("utf-8")).hexdigest()

        # ─────────────────────────────────────
        # Convert Choices into Natively Parsed Structural Trees
        # ─────────────────────────────────────
        from docutils.statemachine import StringList

        for ch in raw_choices:
            # 1. Main Outer Choice Wrap Element (div.multichoice-choice)
            choice_wrap = choice_container_node(correct=ch["correct"])

            # 2. Inside label wrapper element (<label> + div.multichoice-choice-label)
            label_element = choice_label_node(input_type=input_type, group_name=group_name)

            # Sub-parse option text natively into a proxy block container
            text_proxy = nodes.container()
            text_proxy.document = self.state.document
            choice_text_list = StringList(ch["text_lines"], source=self.content.source(0))
            self.state.nested_parse(choice_text_list, self.content_offset, text_proxy)

            label_element.extend(text_proxy.children)
            choice_wrap += label_element

            # 3. Independent Explanation Element (Sits below label, within choice_wrap)
            if ch["explanation_lines"]:
                exp_container = nodes.container(classes=["multichoice-explanation"])
                exp_container.document = self.state.document

                explanation_text_list = StringList(ch["explanation_lines"], source=self.content.source(0))
                self.state.nested_parse(explanation_text_list, self.content_offset, exp_container)

                choice_wrap += exp_container

            node += choice_wrap

        return [node]

# ─────────────────────────────────────
# Setup Configuration Hook
# ─────────────────────────────────────
def setup(app):
    app.add_node(
        multichoice_node,
        html=(visit_multichoice_html, depart_multichoice_html)
    )
    app.add_node(
        choice_container_node,
        html=(visit_choice_container_html, depart_choice_container_html)
    )
    app.add_node(
        choice_label_node,
        html=(visit_choice_label_html, depart_choice_label_html)
    )

    app.add_directive("multichoice", multichoiceDirective)

    static_path = Path(__file__).parent / "_static"
    if str(static_path) not in app.config.html_static_path:
        app.config.html_static_path.append(str(static_path))

    app.add_js_file("multichoice.js")
    app.add_css_file("multichoice.css")

    return {
        "version": "4.2",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }