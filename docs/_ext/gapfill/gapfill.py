import html
import random
import re
from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

class gapfill_node(nodes.General, nodes.Element):
    pass

def visit_gapfill_html(self, node):
    # Retrieve the theme attribute safely directly from the processed node state instance
    chosen_theme = node.get('theme', 'light')
    theme_class = "gapfill-block theme-dark" if chosen_theme == "dark" else "gapfill-block theme-light"

    # Render the wrapper container and its raw code internal layout contents
    self.body.append(f'<div class="{theme_class}">')
    self.body.append(f'<pre class="gapfill-content">{node.get("html_content", "")}</pre>')
    self.body.append('</div>')

    # Crucial structural signal telling Sphinx not to double-process or inspect child nodes
    raise nodes.SkipNode

def depart_gapfill_html(self, node):
    pass


class GapFillDirective(SphinxDirective):
    has_content = True

    option_spec = {
        'theme': directives.unchanged,
    }

    def run(self):
        full_text = "\n".join(self.content)
        node = gapfill_node()

        # Parse theme option (defaults to light configuration rules)
        chosen_theme = self.options.get('theme', 'light').strip().lower()
        if chosen_theme not in ['light', 'dark']:
            chosen_theme = 'light'

        # Safely assign properties to the structural node object instance
        node['theme'] = chosen_theme

        # 1. FIRST PASS: Extract all absolute real answers to use as primary distractors
        all_real_answers = []
        temp_text = full_text
        while "*[" in temp_text and "]*" in temp_text:
            start = temp_text.index("*[")
            end = temp_text.index("]*")
            content = temp_text[start + 2:end].strip()
            real_word = content.split("/")[0].strip()
            if real_word and real_word not in all_real_answers:
                all_real_answers.append(real_word)
            temp_text = temp_text[end + 2:]

        # 2. HARVEST POOL: Extract surrounding prose content to build fallback distractors
        clean_words = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', full_text)
        fallback_pool = list(set([w for w in clean_words if len(w) > 2 and w not in all_real_answers]))

        # 3. SECOND PASS: Construct final interactive HTML layout with select drop-downs
        parsed_html_parts = []
        remaining_text = full_text

        while "*[" in remaining_text and "]*" in remaining_text:
            start_idx = remaining_text.index("*[")
            end_idx = remaining_text.index("]*")

            parsed_html_parts.append(html.escape(remaining_text[:start_idx]))
            content_inner = remaining_text[start_idx + 2:end_idx].strip()

            parts = [p.strip() for p in content_inner.split("/") if p.strip()]
            correct_answer = parts[0]
            explicit_distractors = parts[1:]

            options = {correct_answer}
            for d in explicit_distractors:
                options.add(d)

            # Supplement options dynamically if target threshold isn't met
            needed = 4 - len(options)
            if needed > 0:
                random.shuffle(fallback_pool)
                for candidate in fallback_pool:
                    if candidate not in options:
                        options.add(candidate)
                        needed -= 1
                        if needed == 0:
                            break

            # If still short, supplement from globally harvested correct answers
            if len(options) < 4:
                random.shuffle(all_real_answers)
                for candidate in all_real_answers:
                    if candidate not in options:
                        options.add(candidate)
                        if len(options) == 4:
                            break

            dropdown_html = '<span class="gapfill-wrapper">'
            dropdown_html += f'<select class="gapfill-input gapfill-dropdown" data-correct="{html.escape(correct_answer.lower())}">'
            dropdown_html += '<option value="">-- Choose --</option>'

            for opt in sorted(options, key=str.lower):
                dropdown_html += f'<option value="{html.escape(opt.lower())}">{html.escape(opt)}</option>'
            dropdown_html += '</select>'

            dropdown_html += '<span class="gapfill-inline-feedback"></span>'
            dropdown_html += '</span>'

            parsed_html_parts.append(dropdown_html)
            remaining_text = remaining_text[end_idx + 2:]

        parsed_html_parts.append(html.escape(remaining_text))

        # Re-introduce HTML break syntax for clean multi-line rendering inside the <pre> tag
        combined_html = "".join(parsed_html_parts).replace("\n", "<br>")

        # Save HTML data onto the node container state variables safely
        node['html_content'] = combined_html

        return [node]


def setup(app):
    app.add_node(gapfill_node, html=(visit_gapfill_html, depart_gapfill_html))
    app.add_directive("gapfill", GapFillDirective)

    # 1. Dynamically locate this extension's local static directory
    static_path = Path(__file__).parent / "_static"
    if str(static_path) not in app.config.html_static_path:
        app.config.html_static_path.append(str(static_path))

    # 2. Tell Sphinx to load the file from the flat output root directory
    app.add_js_file("gapfill.js")
    app.add_css_file("gapfill.css")


    return {
        "version": "2.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True
    }
