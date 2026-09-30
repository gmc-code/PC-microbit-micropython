import html
import random
import re
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.directives.code import CodeBlock
from sphinx.util.docutils import SphinxDirective


class cloze_node(nodes.General, nodes.Element):
    pass


def visit_cloze_html(self, node):
    theme_class = node.get("theme", "theme-white")
    self.body.append(f'<div class="cloze-block {theme_class}">')


def depart_cloze_html(self, node):
    self.body.append('</div>')


class ClozeDirective(SphinxDirective):
    has_content = True
    optional_arguments = 1  # Optional language argument (e.g., .. cloze:: python)

    option_spec = {
        'auto-distract': directives.flag,
        'theme': lambda argument: directives.choice(argument, ('white', 'light')),
        'show-code': directives.flag,
        'instructions': directives.unchanged,
        'shuffle-lines': directives.flag,     # Flag to enable line shuffling
        'shuffle': directives.flag,           # Alias for shuffle-lines
    }

    def run(self):
        full_text = "\n".join(self.content).strip()

        # --- AUTO-NUMBERING FIX FOR '#.' ---
        line_counter = 1

        def replace_auto_number(match):
            nonlocal line_counter
            indent = match.group(1)
            formatted = f"{indent}{line_counter}."
            line_counter += 1
            return formatted

        full_text = re.sub(
            r'^(\s*)#\.', replace_auto_number, full_text, flags=re.MULTILINE
        )

        language = self.arguments[0] if self.arguments else "python"
        theme_val = self.options.get('theme', 'white')
        auto_distract = 'auto-distract' in self.options
        show_code = 'show-code' in self.options
        instructions = self.options.get('instructions', '').strip()
        should_shuffle_lines = 'shuffle-lines' in self.options or 'shuffle' in self.options

        if not hasattr(self.env, 'cloze_gap_counter'):
            self.env.cloze_gap_counter = 0

        gap_pattern = re.compile(r'@@([^@]+)@@')

        all_words_in_text = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', full_text)
        context_distractors = list(
            set([w for w in all_words_in_text if len(w) > 2])
        )

        # 1. FIRST PASS: Extract answers and clean markup
        word_bank_items = []

        def extract_words(match):
            raw_content = match.group(1).strip()

            if re.search(r'[|/\\,]', raw_content):
                parts = [
                    p.strip()
                    for p in re.split(r'[|/\\,]', raw_content)
                    if p.strip()
                ]
                correct_answer = parts[0]
                word_bank_items.extend(parts)
                return f"*[ {correct_answer} ]*"
            else:
                word_bank_items.append(raw_content)
                if auto_distract:
                    shuffled_pool = context_distractors.copy()
                    random.shuffle(shuffled_pool)
                    added_count = 0
                    for item in shuffled_pool:
                        if added_count >= 1:
                            break
                        if item != raw_content and item not in word_bank_items:
                            word_bank_items.append(item)
                            added_count += 1

                return f"*[ {raw_content} ]*"

        cleaned_text = gap_pattern.sub(extract_words, full_text)

        clean_full_text = gap_pattern.sub(
            lambda m: re.split(r'[|/\\,]', m.group(1))[0].strip(), full_text
        )
        raw_code_lines = clean_full_text.splitlines()

        # 2. SECOND PASS: Construct HTML nodes layout
        html_gap_pattern = re.compile(r'\*\[\s*(.*?)\s*\]\*')

        def replace_gap(match):
            self.env.cloze_gap_counter += 1
            raw_content = match.group(1).strip()
            final_correct = raw_content
            return (
                f'<span class="cloze-wrapper">'
                f'<span class="cloze-dropzone" data-gap-id="{self.env.cloze_gap_counter}" data-correct="{html.escape(final_correct)}">Drop here</span>'
                f'<span class="cloze-inline-feedback"></span>'
                f'</span>'
            )

        # Process each line individually to preserve layout during line shuffling
        lines = cleaned_text.splitlines()
        processed_lines = []

        for line in lines:
            escaped_line = html.escape(line)
            escaped_line = escaped_line.replace(html.escape("*["), "*[").replace(
                html.escape("]*"), "]*"
            )
            line_html = html_gap_pattern.sub(replace_gap, escaped_line)
            processed_lines.append(line_html)

        # Shuffle lines if option is enabled
        if should_shuffle_lines:
            random.shuffle(processed_lines)

        combined_text_html = "<br>".join(processed_lines)

        word_bank_items.sort()

        # Render custom instructions if provided, otherwise default bank header
        instructions_html = ""
        if instructions:
            instructions_html = f'<div class="cloze-instructions">{html.escape(instructions)}</div>'

        if show_code:
            bank_title_text = "Word Bank (Drag items below). Get 100% to reveal the code for copying:"
        else:
            bank_title_text = "Word Bank (Drag items below):"

        bank_html = f'{instructions_html}<div class="cloze-wordbank-title">{bank_title_text}</div>'

        bank_html += '<div class="cloze-wordbank-tray">'
        for word in word_bank_items:
            bank_html += f'<div class="cloze-draggable" draggable="true" data-word="{html.escape(word)}">{html.escape(word)}</div>'
        bank_html += '</div><hr class="cloze-divider">'

        control_panel_html = """
        <div class="cloze-global-panel">
          <button type="button" class="cloze-btn-score">Score</button>
          <button type="button" class="cloze-btn-reset">Reset</button>
          <span class="cloze-output"></span>
        </div>
        """

        final_html = f'{bank_html}<pre class="cloze-content">{combined_text_html}</pre>{control_panel_html}'

        wrapper_node = cloze_node()
        wrapper_node['theme'] = f"theme-{theme_val}"
        wrapper_node += nodes.raw("", final_html, format="html")

        # 3. Generate hidden Sphinx CodeBlock node if :show-code: flag is set
        if show_code:
            code_block_dir = CodeBlock(
                name='code-block',
                arguments=[language],
                options={},
                content=raw_code_lines,
                lineno=self.lineno,
                content_offset=self.content_offset,
                block_text=self.block_text,
                state=self.state,
                state_machine=self.state_machine,
            )

            code_nodes = code_block_dir.run()

            completed_container = nodes.container(
                classes=['cloze-completed-code']
            )
            completed_container['style'] = 'display: none;'

            heading = nodes.rubric(
                text="Complete code for copying", classes=['cloze-code-heading']
            )
            completed_container += heading
            completed_container.extend(code_nodes)

            wrapper_node += completed_container

        return [wrapper_node]


def setup(app):
    app.add_node(cloze_node, html=(visit_cloze_html, depart_cloze_html))
    app.add_directive("cloze", ClozeDirective)

    static_path = Path(__file__).parent / "_static"
    if str(static_path) not in app.config.html_static_path:
        app.config.html_static_path.append(str(static_path))

    app.add_js_file("cloze.js")
    app.add_css_file("cloze.css")

    return {
        "version": "4.3",
        "parallel_read_safe": True,
        "parallel_write_safe": True
    }