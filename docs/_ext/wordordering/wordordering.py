import html
import random
import re
from pathlib import Path

from docutils import nodes
from docutils.core import publish_parts
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class wordordering_node(nodes.General, nodes.Element):
    pass


def visit_wordordering_html(self, node):
    pass


def depart_wordordering_html(self, node):
    pass


class WordOrderingDirective(SphinxDirective):
    has_content = True
    optional_arguments = 1

    option_spec = {
        'theme': directives.unchanged,
        'instructions': directives.unchanged,  # Added instructions option
        'no-solution': directives.flag,
        'no-padding': directives.flag,
        'no-reorder': directives.flag,
        'delimiter': directives.unchanged,
        'keeprst': directives.flag,
    }

    def render_rst_fragment(self, rst_text):
        """Renders inline RST markup and Sphinx roles to clean HTML fragments."""
        if not rst_text.strip():
            return "&nbsp;"

        parts = publish_parts(
            source=rst_text,
            writer_name='html5',
            settings_spec=None,
            settings_overrides=self.state.document.settings.__dict__
        )

        rendered_html = parts['fragment'].strip()
        if rendered_html.startswith("<p>") and rendered_html.endswith("</p>"):
            rendered_html = rendered_html[3:-4]

        return rendered_html

    def _tokenize_sentence(self, sentence, delimiter=None):
        """Splits a sentence into draggable fragments while protecting inline RST roles."""
        if delimiter:
            return [f.strip() for f in sentence.split(delimiter) if f.strip()]

        role_pattern = r'(:[a-zA-Z0-9_]+:`[^`]+`|\w+|[^\w\s]+)'
        tokens = re.findall(role_pattern, sentence)

        merged_tokens = []
        for token in tokens:
            if merged_tokens and re.match(r'^[.,!?;:]$', token):
                merged_tokens[-1] += token
            else:
                merged_tokens.append(token)

        return merged_tokens

    def _shuffle_guaranteed(self, items):
        """Ensures the shuffled starting state never matches the correct answer key."""
        if len(items) <= 1:
            return items

        original_indices = [item['correct_idx'] for item in items]
        shuffled = items.copy()

        for _ in range(50):
            random.shuffle(shuffled)
            current_indices = [item['correct_idx'] for item in shuffled]
            if current_indices != original_indices:
                break

        return shuffled

    def run(self):
        raw_lines = list(self.content)
        if not raw_lines:
            return []

        full_sentence = " ".join([l.strip() for l in raw_lines if l.strip()])
        if not full_sentence:
            return []

        chosen_theme = self.options.get('theme', 'white').strip().lower()
        if chosen_theme not in ['white', 'light']:
            chosen_theme = 'white'

        hide_solution = 'no-solution' in self.options
        use_no_padding = 'no-padding' in self.options
        no_reorder = 'no-reorder' in self.options
        delimiter = self.options.get('delimiter', None)

        default_instruction = 'Drag and drop the word chips into the correct sentence order:'
        custom_instruction = self.options.get('instructions', default_instruction)
        instruction_text = html.escape(custom_instruction)

        padding_class = ' ordering-no-padding' if use_no_padding else ''

        raw_fragments = self._tokenize_sentence(full_sentence, delimiter=delimiter)

        line_items = []
        for index, fragment in enumerate(raw_fragments):
            line_items.append({
                'correct_idx': index,
                'text': fragment,
                'indent': 0,
                'is_blank': False,
            })

        if not no_reorder:
            processed_items = self._shuffle_guaranteed(line_items)
        else:
            processed_items = line_items.copy()

        main_block_node = nodes.container(
            classes=[f'wordordering-block ordering-block{padding_class}'.strip()])

        html_output = f'<div class="ordering-instructions">{instruction_text}</div>'

        no_reorder_attr = ' data-no-reorder="true"' if no_reorder else ''
        html_output += f'<div class="ordering-container sentence-inline-container theme-{chosen_theme}"{no_reorder_attr}>'

        for item in processed_items:
            display_html = self.render_rst_fragment(item['text'])
            is_draggable = "false" if no_reorder else "true"

            html_output += f'''
            <div class="ordering-line sentence-chip"
                 draggable="{is_draggable}"
                 data-correct-idx="{item['correct_idx']}"
                 data-correct-indent="0"
                 data-current-indent="0"
                 style="--indent-level: 0;">
                <span class="ordering-handle">☰</span>
                <div class="ordering-code">{display_html}</div>
            </div>
            '''
        html_output += '</div>'

        solution_btn_style = 'style="display: none !important;"' if hide_solution else ''
        html_output += f'''
        <div class="ordering-controls">
            <button type="button" class="ordering-btn-score">Check</button>
            <button type="button" class="ordering-btn-continue" style="display: none;">Continue</button>
            <button type="button" class="ordering-btn-solution" {solution_btn_style}>Show Solution</button>
            <button type="button" class="ordering-btn-reset">Reset</button>
            <span class="ordering-feedback-badge"></span>
        </div>
        '''

        raw_interactive_node = nodes.raw("", html_output, format="html")
        main_block_node += raw_interactive_node

        return [main_block_node]


def setup(app):
    app.add_node(wordordering_node,
                 html=(visit_wordordering_html, depart_wordordering_html))
    app.add_directive("wordordering", WordOrderingDirective)

    static_path = Path(__file__).parent / "_static"
    if str(static_path) not in app.config.html_static_path:
        app.config.html_static_path.append(str(static_path))

    app.add_js_file("wordordering.js")
    app.add_css_file("wordordering.css")
    return {
        "version": "1.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True
    }