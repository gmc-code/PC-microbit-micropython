import html
import random
import re
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

class cloze_node(nodes.General, nodes.Element):
    pass

def visit_cloze_html(self, node):
    theme_class = node.get("theme", "theme-light")
    self.body.append(f'<div class="cloze-block {theme_class}">')

def depart_cloze_html(self, node):
    self.body.append('</div>')


class ClozeDirective(SphinxDirective):
    has_content = True

    option_spec = {
        'auto-distract': directives.flag,
        'theme': lambda argument: directives.choice(argument, ('light', 'dark')),
    }

    def run(self):
        full_text = "\n".join(self.content).strip()
        node = cloze_node()

        theme_val = self.options.get('theme', 'light')
        node['theme'] = f"theme-{theme_val}"

        auto_distract = 'auto-distract' in self.options
        gap_pattern = re.compile(r'\*\[(.*?)\]\*')

        # 1. FIRST PASS: Extract answers and clean markup
        word_bank_items = []
        gap_counter = 0

        def extract_words(match):
            nonlocal gap_counter
            gap_counter += 1
            raw_content = match.group(1)

            # SUPPORT MULTIPLE SEPARATORS: matches |, /, \, or ,
            if re.search(r'[|/\\,]', raw_content):
                # Split on any of the delimiters and strip spaces around each item
                parts = [p.strip() for p in re.split(r'[|/\\,]', raw_content)]
                correct_answer = parts[0] # The first item is always treated as correct
                word_bank_items.extend(parts)
                return f"*[ {correct_answer} ]*"
            else:
                word_bank_items.append(raw_content)
                return f"*[ {raw_content} ]*"

        cleaned_text = gap_pattern.sub(extract_words, full_text)

        # 2. SECOND PASS: Construct HTML nodes layout
        gap_counter = 0

        def replace_gap(match):
            nonlocal gap_counter
            gap_counter += 1
            raw_content = match.group(1).strip()

            final_correct = raw_content
            drop_zone_html = f'<span class="cloze-wrapper"><span class="cloze-dropzone" data-gap-id="{gap_counter}" data-correct="{html.escape(final_correct.lower())}">Drop here</span><span class="cloze-inline-feedback"></span></span>'
            return drop_zone_html

        escaped_text = html.escape(cleaned_text)
        escaped_text = escaped_text.replace(html.escape("*["), "*[").replace(html.escape("]*"), "]*")

        combined_text_html = gap_pattern.sub(replace_gap, escaped_text)
        combined_text_html = combined_text_html.replace("\n", "<br>")

        word_bank_items = list(set(word_bank_items))
        random.shuffle(word_bank_items)

        bank_html = '<div class="cloze-wordbank-title">Word Bank (Drag items below):</div>'
        bank_html += '<div class="cloze-wordbank-tray">'
        for word in word_bank_items:
            bank_html += f'<div class="cloze-draggable" draggable="true" data-word="{html.escape(word.lower())}">{html.escape(word)}</div>'
        bank_html += '</div><hr class="cloze-divider">'

        # Localized control panels (matches section-scoped configuration)
        control_panel_html = '''
        <div class="cloze-global-panel">
          <button type="button" class="cloze-btn-score">Score Section</button>
          <button type="button" class="cloze-btn-reset">Reset Section</button>
          <span class="cloze-output"></span>
        </div>
        '''

        final_html = f'{bank_html}<pre class="cloze-content">{combined_text_html}</pre>{control_panel_html}'
        node += nodes.raw("", final_html, format="html")

        return [node]



def setup(app):
    app.add_node(cloze_node, html=(visit_cloze_html, depart_cloze_html))
    app.add_directive("cloze", ClozeDirective)

    # 1. Dynamically locate this extension's local static directory
    static_path = Path(__file__).parent / "_static"
    if str(static_path) not in app.config.html_static_path:
        app.config.html_static_path.append(str(static_path))

    # 2. Tell Sphinx to load the file from the flat output root directory
    app.add_js_file("cloze.js")
    app.add_css_file("cloze.css")

    return {
        "version": "3.8",
        "parallel_read_safe": True,
        "parallel_write_safe": True
    }
