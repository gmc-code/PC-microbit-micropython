import html
import re
from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

class fillin_node(nodes.General, nodes.Element):
    pass

def visit_fillin_html(self, node):
    chosen_theme = node.get('theme', 'white')
    theme_class = "fillin-block theme-light" if chosen_theme == "light" else "fillin-block theme-white"

    self.body.append(f'<div class="{theme_class}">')
    self.body.append('<div class="fillin-instructions">Type in the missing words to fill in the gaps below:</div>')
    self.body.append(f'<pre class="fillin-content">{node.get("html_content", "")}</pre>')
    self.body.append('</div>')
    raise nodes.SkipNode

def depart_fillin_html(self, node):
    pass


class FillInDirective(SphinxDirective):
    has_content = True

    option_spec = {
        'theme': directives.unchanged,
        'case_sensitive': directives.flag,
    }

    def run(self):
        full_text = "\n".join(self.content)
        node = fillin_node()

        chosen_theme = self.options.get('theme', 'white').strip().lower()
        if chosen_theme not in ['white', 'light']:
            chosen_theme = 'white'
        node['theme'] = chosen_theme

        case_sensitive = 'case_sensitive' in self.options
        node['case_sensitive'] = case_sensitive

        gap_pattern = re.compile(r'@@([^@]+)@@')
        parsed_html_parts = []
        remaining_text = full_text

        while True:
            match = gap_pattern.search(remaining_text)
            if not match:
                break

            start_idx, end_idx = match.span()
            parsed_html_parts.append(html.escape(remaining_text[:start_idx]))

            correct_answer = match.group(1).strip()

            if not correct_answer:
                parsed_html_parts.append(html.escape(match.group(0)))
                remaining_text = remaining_text[end_idx:]
                continue

            # Calculate input field size based on answer length
            input_size = max(len(correct_answer) + 3, 8)

            input_html = f'<span class="fillin-wrapper">'
            input_html += f'<input type="text" class="fillin-text-input fillin-input" '
            input_html += f'data-correct="{html.escape(correct_answer)}" '
            input_html += f'data-case-sensitive="{ "true" if case_sensitive else "false" }" '
            input_html += f'size="{input_size}" placeholder="..." />'
            input_html += '<span class="fillin-inline-feedback"></span>'
            input_html += '</span>'

            parsed_html_parts.append(input_html)
            remaining_text = remaining_text[end_idx:]

        parsed_html_parts.append(html.escape(remaining_text))
        combined_html = "".join(parsed_html_parts).replace("\n", "<br>")
        node['html_content'] = combined_html

        return [node]


def setup(app):
    app.add_node(fillin_node, html=(visit_fillin_html, depart_fillin_html))
    app.add_directive("fillin", FillInDirective)

    static_path = Path(__file__).parent / "_static"
    if str(static_path) not in app.config.html_static_path:
        app.config.html_static_path.append(str(static_path))

    app.add_js_file("fillin.js")
    app.add_css_file("fillin.css")
    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True
    }