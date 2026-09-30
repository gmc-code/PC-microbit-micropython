import html
import hashlib
from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives, DirectiveError
from sphinx.util.docutils import SphinxDirective
from docutils.statemachine import StringList


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
    torf_attr = str(node.get("torf", False)).lower()
    theme_attr = node.get("theme", "white")

    self.body.append(
        f'<div class="multichoice-block theme-{theme_attr}" '
        f'data-multichoice-single="{single_attr}" '
        f'data-multichoice-shuffle="{shuffle_attr}" '
        f'data-multichoice-torf="{torf_attr}" '
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
        "torf": directives.flag,  # True or False flag option
        "theme": lambda argument: directives.choice(argument, ("white", "light")),
        "delimiter": directives.unchanged,
    }

    def run(self):
        node = multichoice_node()

        is_torf = "torf" in self.options
        node["torf"] = is_torf

        # Core configuration options (True/False mode disables shuffling)
        node["shuffle"] = False if is_torf else ("no-shuffle" not in self.options)
        node["letters"] = "no-letters" not in self.options

        chosen_theme = self.options.get("theme", "white").strip().lower()
        if chosen_theme not in ["white", "light"]:
            chosen_theme = "white"
        node["theme"] = chosen_theme

        delimiter = self.options.get("delimiter", "|")

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
        # Parse Question
        # ─────────────────────────────────────
        question_container = nodes.container(classes=["multichoice-question"])
        self.state.nested_parse(question_lines, self.content_offset, question_container)
        node += question_container

        # ─────────────────────────────────────
        # Parse Choices
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

                if delimiter in content_start:
                    txt, exp = content_start.split(delimiter, 1)
                    if txt.strip():
                        current_choice["text_lines"].append(txt)
                    if exp.strip():
                        current_choice["explanation_lines"].append(exp)
                    current_choice["in_explanation"] = True
                else:
                    if content_start.strip():
                        current_choice["text_lines"].append(content_start)

            elif current_choice is not None:
                if delimiter in line:
                    txt, exp = line.split(delimiter, 1)
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

        # ─────────────────────────────────────
        # True/False Ordering Adjustment
        # ─────────────────────────────────────
        if is_torf:
            def is_true_choice(c):
                text = " ".join(c["text_lines"]).strip().lower()
                return text.startswith("true") or text.startswith("t")

            true_choices = [c for c in raw_choices if is_true_choice(c)]
            other_choices = [c for c in raw_choices if not is_true_choice(c)]
            raw_choices = true_choices + other_choices

        correct_count = sum(c["correct"] for c in raw_choices)
        if correct_count == 0:
            raise DirectiveError(3, "MCQ error: Must mark at least one option correct [x].")

        is_multi = correct_count > 1
        node["single_correct"] = not is_multi
        input_type = "checkbox" if is_multi else "radio"

        seed_string = "".join("".join(c["text_lines"]) for c in raw_choices)
        group_name = hashlib.md5(seed_string.encode("utf-8")).hexdigest()

        # ─────────────────────────────────────
        # Construct Nodes
        # ─────────────────────────────────────
        def normalize_line_blocks(lines):
            cleaned = []
            for l in lines:
                stripped = l.strip()
                if stripped.startswith("|"):
                    content = stripped[1:].strip()
                    cleaned.append(f"| {content}")
                else:
                    cleaned.append(l)
            return cleaned

        for ch in raw_choices:
            choice_wrap = choice_container_node(correct=ch["correct"])
            label_element = choice_label_node(input_type=input_type, group_name=group_name)

            text_lines = normalize_line_blocks(ch["text_lines"])
            text_proxy = nodes.container()
            text_proxy.document = self.state.document
            choice_text_list = StringList(text_lines, source=self.content.source(0))
            self.state.nested_parse(choice_text_list, self.content_offset, text_proxy)

            label_element.extend(text_proxy.children)
            choice_wrap += label_element

            if ch["explanation_lines"]:
                exp_container = nodes.container(classes=["multichoice-explanation"])
                exp_container.document = self.state.document
                exp_lines = normalize_line_blocks(ch["explanation_lines"])
                explanation_text_list = StringList(exp_lines, source=self.content.source(0))
                self.state.nested_parse(explanation_text_list, self.content_offset, exp_container)

                choice_wrap += exp_container

            node += choice_wrap

        return [node]


def setup(app):
    app.add_node(multichoice_node, html=(visit_multichoice_html, depart_multichoice_html))
    app.add_node(choice_container_node, html=(visit_choice_container_html, depart_choice_container_html))
    app.add_node(choice_label_node, html=(visit_choice_label_html, depart_choice_label_html))

    app.add_directive("multichoice", multichoiceDirective)

    static_path = Path(__file__).parent / "_static"
    if str(static_path) not in app.config.html_static_path:
        app.config.html_static_path.append(str(static_path))

    app.add_js_file("multichoice.js")
    app.add_css_file("multichoice.css")

    return {
        "version": "4.4",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }