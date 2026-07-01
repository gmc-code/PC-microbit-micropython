import html
import hashlib
from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives, DirectiveError
from sphinx.util.docutils import SphinxDirective

# ─────────────────────────────────────
# Node
# ─────────────────────────────────────
class multichoice_node(nodes.General, nodes.Element):
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

        # Core options
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
        # Robust Multi-line Choice Parser
        # ─────────────────────────────────────
        choices = []
        current_choice = None
        in_explanation_mode = False

        for line in choice_lines:
            stripped = line.strip()

            # Case 1: Detect a brand new choice starting block
            if stripped.startswith("[") and "]" in stripped:
                marker = stripped[1].lower()
                is_correct = marker == "x"

                raw_text = stripped[stripped.index("]") + 1:].strip()

                # Check if an explanation starts on this very first line
                if "|" in raw_text:
                    text, explanation = raw_text.split("|", 1)
                    text = text.strip()
                    explanation = explanation.strip()
                    in_explanation_mode = True
                else:
                    text = raw_text
                    explanation = ""
                    in_explanation_mode = False

                current_choice = {
                    "text": text,
                    "correct": is_correct,
                    "explanation": explanation
                }
                choices.append(current_choice)

            # Case 2: Continuation lines (Multi-line text or multi-line explanation)
            elif current_choice is not None and stripped:
                if "|" in stripped:
                    text_part, exp_part = stripped.split("|", 1)

                    if text_part.strip():
                        current_choice["text"] += " " + text_part.strip()

                    current_choice["explanation"] = exp_part.strip()
                    in_explanation_mode = True
                else:
                    if in_explanation_mode:
                        if current_choice["explanation"]:
                            current_choice["explanation"] += " " + stripped
                        else:
                            current_choice["explanation"] = stripped
                    else:
                        current_choice["text"] += " " + stripped

        # Clean up any trailing whitespace strings from empty explanation nodes
        for ch in choices:
            ch["explanation"] = ch["explanation"].strip() if ch["explanation"] else None

        # ─────────────────────────────────────
        # Validation & Auto-Mode Selection
        # ─────────────────────────────────────
        if not choices:
            raise DirectiveError(3, "MCQ error: Missing answer choices block.")

        correct_count = sum(c["correct"] for c in choices)
        if correct_count == 0:
            raise DirectiveError(3, "MCQ error: Must mark at least one option correct [x].")

        is_multi = correct_count > 1
        node["single_correct"] = not is_multi

        seed_string = "".join(c["text"] for c in choices)
        group_name = hashlib.md5(seed_string.encode("utf-8")).hexdigest()

        # ─────────────────────────────────────
        # Generate Choice Elements HTML
        # ─────────────────────────────────────
        input_type = "checkbox" if is_multi else "radio"

        for ch in choices:
            input_html = f'<input type="{input_type}" name="multichoice-{group_name}">'

            html_str = f'''
<div class="multichoice-choice" data-correct="{str(ch["correct"]).lower()}">
  <label>
    {input_html}
    <span class="multichoice-letter"></span>
    <span class="multichoice-choice-label">{html.escape(ch["text"])}</span>
  </label>
'''
            if ch["explanation"]:
                html_str += (
                    f'<div class="multichoice-explanation">'
                    f'{html.escape(ch["explanation"])}'
                    f'</div>'
                )

            html_str += "</div>"
            node += nodes.raw("", html_str, format="html")

        return [node]

# ─────────────────────────────────────
# Setup
# ─────────────────────────────────────
def setup(app):
    app.add_node(
        multichoice_node,
        html=(visit_multichoice_html, depart_multichoice_html)
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