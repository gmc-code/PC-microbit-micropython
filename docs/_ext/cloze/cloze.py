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

        # Updated regex to match @@ content @@ safely without breaking python lists [...]
        gap_pattern = re.compile(r'@@([^@]+)@@')

        # Extract all potential words from the sentence context to use as distractors
        # We strip away syntax tokens and find unique words longer than 2 characters
        all_words_in_text = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', full_text)
        context_distractors = list(set([w for w in all_words_in_text if len(w) > 2]))

        # 1. FIRST PASS: Extract answers and clean markup
        word_bank_items = []
        gap_counter = 0

        def extract_words(match):
            nonlocal gap_counter
            gap_counter += 1

            raw_content = match.group(1).strip()

            # SUPPORT MULTIPLE SEPARATORS: matches |, /, \, or ,
            if re.search(r'[|/\\,]', raw_content):
                parts = [p.strip() for p in re.split(r'[|/\\,]', raw_content) if p.strip()]
                correct_answer = parts[0]
                word_bank_items.extend(parts)
                return f"*[ {correct_answer} ]*"
            else:
                word_bank_items.append(raw_content)

                # FIXED LOGIC: Extract distractors directly from the surrounding text context
                if auto_distract:
                    shuffled_pool = context_distractors.copy()
                    random.shuffle(shuffled_pool)
                    added_count = 0
                    for item in shuffled_pool:
                        if added_count >= 1:  # Add up to 1 distractors from the sentence
                            break
                        # Enforce strict casing mismatch checks and make sure it's not already in the bank
                        if item.lower() != raw_content.lower() and item.lower() not in [w.lower() for w in word_bank_items]:
                            word_bank_items.append(item)
                            added_count += 1

                return f"*[ {raw_content} ]*"

        cleaned_text = gap_pattern.sub(extract_words, full_text)

        # 2. SECOND PASS: Construct HTML nodes layout
        gap_counter = 0
        html_gap_pattern = re.compile(r'\*\[\s*(.*?)\s*\]\*')

        def replace_gap(match):
            nonlocal gap_counter
            gap_counter += 1
            raw_content = match.group(1).strip()

            final_correct = raw_content
            drop_zone_html = f'<span class="cloze-wrapper"><span class="cloze-dropzone" data-gap-id="{gap_counter}" data-correct="{html.escape(final_correct.lower())}">Drop here</span><span class="cloze-inline-feedback"></span></span>'
            return drop_zone_html

        escaped_text = html.escape(cleaned_text)
        escaped_text = escaped_text.replace(html.escape("*["), "*[").replace(html.escape("]*"), "]*")

        combined_text_html = html_gap_pattern.sub(replace_gap, escaped_text)
        combined_text_html = combined_text_html.replace("\n", "<br>")

        word_bank_items = list(set(word_bank_items))
        random.shuffle(word_bank_items)

        bank_html = '<div class="cloze-wordbank-title">Word Bank (Drag items below):</div>'
        bank_html += '<div class="cloze-wordbank-tray">'
        for word in word_bank_items:
            bank_html += f'<div class="cloze-draggable" draggable="true" data-word="{html.escape(word.lower())}">{html.escape(word)}</div>'
        bank_html += '</div><hr class="cloze-divider">'

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

    static_path = Path(__file__).parent / "_static"
    if str(static_path) not in app.config.html_static_path:
        app.config.html_static_path.append(str(static_path))

    app.add_js_file("cloze.js")
    app.add_css_file("cloze.css")

    return {
        "version": "4.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True
    }