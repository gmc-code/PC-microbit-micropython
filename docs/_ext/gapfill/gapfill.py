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
    chosen_theme = node.get('theme', 'light')
    theme_class = "gapfill-block theme-dark" if chosen_theme == "dark" else "gapfill-block theme-light"

    self.body.append(f'<div class="{theme_class}">')
    self.body.append(f'<pre class="gapfill-content">{node.get("html_content", "")}</pre>')
    self.body.append('</div>')
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

        chosen_theme = self.options.get('theme', 'light').strip().lower()
        if chosen_theme not in ['light', 'dark']:
            chosen_theme = 'light'
        node['theme'] = chosen_theme

        # Harvest potential distractors directly from the text block context (ignoring syntax)
        all_words_in_text = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', full_text)
        context_distractors = list(set([w for w in all_words_in_text if len(w) > 2]))

        # Updated regex to match @@ choice1 | choice2 @@ syntax securely without touching Python lists [...]
        gap_pattern = re.compile(r'@@([^@]+)@@')
        parsed_html_parts = []
        remaining_text = full_text

        while True:
            match = gap_pattern.search(remaining_text)
            if not match:
                break

            start_idx, end_idx = match.span()
            parsed_html_parts.append(html.escape(remaining_text[:start_idx]))

            # Isolate content within the @@ delimiters and clean internal spaces
            raw_choices_str = match.group(1).strip()

            # Split exclusively on vertical pipes '|'
            if '|' in raw_choices_str:
                raw_options = [opt.strip() for opt in raw_choices_str.split('|') if opt.strip()]
            else:
                raw_options = [raw_choices_str] if raw_choices_str else []

            if not raw_options:
                parsed_html_parts.append(html.escape(match.group(0)))
                remaining_text = remaining_text[end_idx:]
                continue

            correct_answer = raw_options[0]
            options = set(raw_options)

            # If exactly 1 option is provided, extract exactly 1 distractor from the question text
            if len(raw_options) == 1:
                shuffled_pool = context_distractors.copy()
                random.shuffle(shuffled_pool)
                for alt in shuffled_pool:
                    if alt != correct_answer and alt not in options:
                        options.add(alt)
                        break

            # Build dropdown markup container node
            dropdown_html = f'<span class="gapfill-wrapper">'
            dropdown_html += f'<select class="gapfill-dropdown gapfill-input" data-correct="{html.escape(correct_answer)}">'
            dropdown_html += '<option value="">-- Choose --</option>'

            # Sort items in their exact specified casing styles cleanly
            for opt in sorted(options, key=str.lower):
                dropdown_html += f'<option value="{html.escape(opt)}">{html.escape(opt)}</option>'
            dropdown_html += '</select>'

            dropdown_html += '<span class="gapfill-inline-feedback"></span>'
            dropdown_html += '</span>'

            parsed_html_parts.append(dropdown_html)
            remaining_text = remaining_text[end_idx:]

        parsed_html_parts.append(html.escape(remaining_text))
        combined_html = "".join(parsed_html_parts).replace("\n", "<br>")
        node['html_content'] = combined_html

        return [node]


def setup(app):
    app.add_node(gapfill_node, html=(visit_gapfill_html, depart_gapfill_html))
    app.add_directive("gapfill", GapFillDirective)

    static_path = Path(__file__).parent / "_static"
    if str(static_path) not in app.config.html_static_path:
        app.config.html_static_path.append(str(static_path))

    app.add_js_file("gapfill.js")
    app.add_css_file("gapfill.css")
    return {
        "version": "2.9",
        "parallel_read_safe": True,
        "parallel_write_safe": True
    }