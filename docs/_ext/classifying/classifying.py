import html
import random
import re
from pathlib import Path

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
        'bins': directives.unchanged,         # Explicit comma-separated list of categories
        'instructions': directives.unchanged, # Custom instruction text override
        'delimiter': directives.unchanged,    # Custom separator e.g., '=>', '::', '|'
        'sep': directives.unchanged,          # Alias for delimiter
        'shuffle': directives.flag,
        'nosort': directives.flag,
        'sort': directives.unchanged,
        'solution': directives.unchanged,     # Accepts "true"/"false" or flag
    }

    @staticmethod
    def format_rst_markup(text):
        """Converts rST roles like :process:`word` into HTML markup."""
        role_pattern = re.compile(r':([a-zA-Z0-9_-]+):`([^`]+)`')

        last_end = 0
        formatted_parts = []

        for match in role_pattern.finditer(text):
            plain_prefix = text[last_end:match.start()]
            formatted_parts.append(html.escape(plain_prefix))

            role_name = html.escape(match.group(1))
            role_content = html.escape(match.group(2))

            # Clean inline element without printing the literal role prefix tag
            formatted_parts.append(
                f'<span class="rst-role rst-role-{role_name} {role_name}">'
                f'<code class="rst-role-content">{role_content}</code>'
                f'</span>')
            last_end = match.end()

        formatted_parts.append(html.escape(text[last_end:]))
        return "".join(formatted_parts)

    def run(self):
        node = sorting_node()
        raw_lines = [line.strip() for line in self.content if line.strip()]

        if not raw_lines:
            return []

        # Determine delimiter (defaults to rsplit on ':' from the right if unassigned)
        delimiter = self.options.get('delimiter',
                                     self.options.get('sep', '')).strip()

        # 1. Parse Items and Categories
        parsed_items = []
        collected_categories = []

        for line in raw_lines:
            item_text = ""
            category = ""

            if delimiter and delimiter in line:
                item_text, category = line.split(delimiter, 1)
            elif ":" in line:
                # Use right-split (rsplit) so colons inside roles like :process:`go` aren't split incorrectly
                item_text, category = line.rsplit(":", 1)
            else:
                continue

            item_text = item_text.strip()
            category = category.strip()

            parsed_items.append({'text': item_text, 'category': category})

            if category not in collected_categories:
                collected_categories.append(category)

        # 2. Resolve Bin Names
        bin_option = self.options.get('bins', '')
        if bin_option:
            bin_names = [b.strip() for b in bin_option.split(',')]
        else:
            bin_names = sorted(collected_categories, key=lambda s: s.lower())

        # Map categories to their bin indices
        items = []
        for item in parsed_items:
            category = item['category']
            bin_idx = bin_names.index(category) if category in bin_names else 0
            items.append({'text': item['text'], 'correct_bin': bin_idx})

        # 3. Handle Sorting / Shuffling & Options
        chosen_theme = self.options.get('theme', 'white').strip().lower()
        if chosen_theme not in ['light', 'white']:
            chosen_theme = 'white'

        instructions_text = self.options.get(
            'instructions',
            'Classify each item into its correct category:').strip()

        sort_opt = self.options.get('sort', '').strip().lower()
        if 'nosort' in self.options or sort_opt in ['false', 'no', '0']:
            should_shuffle = False
        else:
            should_shuffle = True

        if should_shuffle:
            random.shuffle(items)

        shuffle_attr = "true" if should_shuffle else "false"

        # Check solution option (flag or explicit boolean)
        solution_opt = self.options.get('solution', '').strip().lower()
        show_solution = 'solution' in self.options or solution_opt in [
            'true', 'yes', '1', ''
        ]

        # 4. Generate HTML Output
        html_output = f'<div class="classifying-block {chosen_theme}">'
        html_output += f'<div class="classifying-instructions">{html.escape(instructions_text)}</div>'
        html_output += f'<div class="classifying-container" data-shuffle="{shuffle_attr}">'

        for item in items:
            formatted_item_html = self.format_rst_markup(item['text'])
            html_output += f'''
            <div class="classifying-line">
                <span class="classifying-code">{formatted_item_html}</span>
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

        # Control panel with Solution button
        solution_btn_html = '<button type="button" class="classifying-btn-solution">Solution</button>' if show_solution else ''

        html_output += f'''
        <div class="classifying-controls">
            <button type="button" class="classifying-btn-score">Check</button>
            {solution_btn_html}
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

    static_path = Path(__file__).parent / "_static"
    if str(static_path) not in app.config.html_static_path:
        app.config.html_static_path.append(str(static_path))

    app.add_js_file("classifying.js")
    app.add_css_file("classifying.css")

    return {
        "version": "1.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True
    }
