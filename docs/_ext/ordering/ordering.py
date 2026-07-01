import html
import random
import re
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

class ordering_node(nodes.General, nodes.Element):
    pass

def visit_ordering_html(self, node):
    pass

def depart_ordering_html(self, node):
    pass

class OrderingDirective(SphinxDirective):
    has_content = True

    option_spec = {
        'theme': directives.unchanged,
        'no-solution': directives.flag,  # Registers the boolean flag option
    }

    def run(self):
        node = ordering_node()
        # Keep ALL lines, including blank ones (do not filter out empty strings)
        raw_lines = list(self.content)

        if not raw_lines:
            return []

        chosen_theme = self.options.get('theme', 'light').strip().lower()
        if chosen_theme not in ['light', 'dark']:
            chosen_theme = 'light'

        # Check if the :no-solution: flag was provided in rST
        hide_solution = 'no-solution' in self.options

        # FIXED: Safe inline style variable that keeps JS happy but hides the button visually
        solution_btn_style = 'style="display: none !important;"' if hide_solution else ''

        line_items = []
        for index, line in enumerate(raw_lines):
            # If the line is purely whitespace, treat it as a structural empty line
            is_blank = not line.strip()

            leading_spaces = len(line) - len(line.lstrip())
            indent_level = 0 if is_blank else (leading_spaces // 4)

            line_items.append({
                'correct_idx': index,
                'text': line.strip() if not is_blank else "",
                'indent': indent_level,
                'is_blank': is_blank
            })

        shuffled_items = line_items.copy()
        random.shuffle(shuffled_items)

        html_output = '<div class="ordering-block">'
        html_output += '<div class="ordering-instructions">Drag and drop lines into the correct order and click to adjust indentation:</div>'
        html_output += f'<div class="ordering-container theme-{chosen_theme}">'

        for item in shuffled_items:
            if item['is_blank']:
                display_text = " "
                extra_class = " blank-line-placeholder"
            else:
                display_text = html.escape(item['text'])
                extra_class = ""

            html_output += f'''
            <div class="ordering-line{extra_class}"
                 draggable="true"
                 data-correct-idx="{item['correct_idx']}"
                 data-correct-indent="{item['indent']}"
                 data-current-indent="0"
                 style="--indent-level: 0;">
                <span class="ordering-handle">☰</span>
                <code class="ordering-code">{display_text}</code>
                <div class="ordering-indent-controls">
                    <button type="button" class="indent-btn decrease" title="Decrease Indent">«</button>
                    <button type="button" class="indent-btn increase" title="Increase Indent">»</button>
                </div>
            </div>
            '''
        html_output += '</div>'

        # Control panel containing the safely hidden inline solution button
        html_output += f'''
        <div class="ordering-controls">
            <button type="button" class="ordering-btn-score">Check Order</button>
            <button type="button" class="ordering-btn-solution" {solution_btn_style}>Show Solution</button>
            <button type="button" class="ordering-btn-reset">Reset</button>
            <span class="ordering-feedback-badge"></span>
        </div>
        '''
        html_output += '</div>'  # Closes the ordering-block container div cleanly

        node += nodes.raw("", html_output, format="html")
        return [node]


def setup(app):
    app.add_node(ordering_node, html=(visit_ordering_html, depart_ordering_html))
    app.add_directive("ordering", OrderingDirective)
    app.add_js_file("ordering.js")
    app.add_css_file("ordering.css")
    return {"version": "1.4", "parallel_read_safe": True, "parallel_write_safe": True}