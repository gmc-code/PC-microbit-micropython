import html
import random
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

class sorting_node(nodes.General, nodes.Element):
    pass

def visit_sorting_html(self, node):
    pass

def depart_sorting_html(self, node):
    pass

class classifyingDirective(SphinxDirective):
    has_content = True

    option_spec = {
        'theme': directives.unchanged,
        'bins': directives.unchanged, # Expects a comma-separated list of 2 to 4 bins
    }

    def run(self):
        node = sorting_node()
        raw_lines = [line.strip() for line in self.content if line.strip()]

        if not raw_lines:
            return []

        # 1. Parse Bins (Support 2, 3, or 4 bins dynamically)
        bin_option = self.options.get('bins', 'Bin 1, Bin 2')
        bin_names = [b.strip() for b in bin_option.split(',')]

        chosen_theme = self.options.get('theme', 'light').strip().lower()
        if chosen_theme not in ['light', 'dark']:
            chosen_theme = 'light'

        # 2. Parse Items and their correct bin assignments
        items = []
        for line in raw_lines:
            if "|" in line:
                item_text, correct_bin_idx = line.split("|", 1)
                items.append({
                    'text': item_text.strip(),
                    'correct_bin': int(correct_bin_idx.strip())
                })

        # Shuffle the items so they don't appear in order
        random.shuffle(items)

        # 3. Generate HTML Output inside your Container (Theme class attached to outer block)
        html_output = f'<div class="classifying-block {chosen_theme}">'
        html_output += '<div class="classifying-instructions">Classify each item into its correct category:</div>'
        html_output += '<div class="classifying-container">' # Removed theme-dark from here

        for item in items:
            html_output += f'''
            <div class="classifying-line">
                <span class="classifying-code">{html.escape(item['text'])}</span>
                <div class="classifying-indent-controls" style="margin-left: auto;">
                    <select class="sorting-select" data-correct-bin="{item['correct_bin']}">
                        <option value="">-- Select Bin --</option>
            '''

            for idx, bin_name in enumerate(bin_names):
                html_output += f'<option value="{idx}">{html.escape(bin_name)}</option>'

            html_output += f'''
                    </select>
                </div>
            </div>
            '''
        html_output += '</div>'

        # Control panel seamlessly adopting your layout specs
        html_output += '''
        <div class="classifying-controls">
            <button type="button" class="classifying-btn-score">Check</button>
            <button type="button" class="classifying-btn-reset">Reset</button>
            <span class="classifying-feedback-badge"></span>
        </div>
        </div>
        '''

        node += nodes.raw("", html_output, format="html")
        return [node]


def setup(app):
    app.add_node(sorting_node, html=(visit_sorting_html, depart_sorting_html))
    app.add_directive("classifying", classifyingDirective)

    # Make sure these match your newly renamed files!
    app.add_js_file("classifying.js")
    app.add_css_file("classifying.css")

    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}