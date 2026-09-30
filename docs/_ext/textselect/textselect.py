import html
import json
import re
from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class textselect_node(nodes.General, nodes.Element):
    pass


def visit_textselect_html(self, node):
    chosen_theme = node.get("theme", "")
    chosen_color = node.get("color", "blue")
    chosen_style = node.get("style", "filled")
    mode = node.get("mode", "single")
    shuffle = "true" if node.get("shuffle", False) else "false"

    theme_class = f"theme-{chosen_theme}" if chosen_theme else ""
    color_class = f"ts-color-{chosen_color}" if mode == "single" else ""
    style_class = f"ts-style-{chosen_style}"
    mode_class = f"ts-mode-{mode}"

    classes = " ".join(
        filter(
            None,
            ["textselect-block", theme_class, color_class, style_class, mode_class],
        )
    )

    self.body.append(
        f'<div class="{classes}" data-mode="{mode}" data-shuffle="{shuffle}">'
    )
    self.body.append(
        f'<div class="textselect-instructions">{node.get("instructions", "")}</div>'
    )
    self.body.append(
        f'<pre class="textselect-content" data-targets=\'{node.get("target_json", "{}")}\'>'
    )
    self.body.append(node.get("html_content", ""))
    self.body.append("</pre></div>")
    raise nodes.SkipNode


def depart_textselect_html(self, node):
    pass


class TextSelectDirective(SphinxDirective):
    has_content = True

    option_spec = {
        "mode": directives.unchanged,
        "theme": directives.unchanged,
        "instructions": directives.unchanged,
        "color": directives.unchanged,
        "style": directives.unchanged,
        "shuffle": directives.flag,
    }

    def run(self):
        full_text = "\n".join(self.content)
        node = textselect_node()
        node["shuffle"] = "shuffle" in self.options

        chosen_mode = self.options.get("mode", "single").strip().lower()
        if chosen_mode not in ["single", "multi"]:
            chosen_mode = "single"
        node["mode"] = chosen_mode

        VALID_THEMES = ["white", "light"]
        chosen_theme = self.options.get("theme", "white").strip().lower()
        if chosen_theme not in VALID_THEMES:
            chosen_theme = "white"
        node["theme"] = chosen_theme

        chosen_color = self.options.get("color", "blue").strip().lower()
        node["color"] = chosen_color

        chosen_style = self.options.get("style", "filled").strip().lower()
        if chosen_style not in ["plain", "border", "filled"]:
            chosen_style = "filled"
        node["style"] = chosen_style

        default_instructions = (
            "Click or drag to highlight the target words."
            if chosen_mode == "single"
            else "Select a color and highlight the corresponding text."
        )
        node["instructions"] = html.escape(
            self.options.get("instructions", default_instructions)
        )

        target_colors = {}
        # FIX: Reset word token index to 0 for EACH directive instance
        word_token_index = 0

        # Split text into lines so JavaScript can shuffle line blocks individually
        lines = full_text.splitlines()
        html_lines = []

        def parse_nested_text(text, active_colors, html_tokens):
            nonlocal word_token_index
            i = 0
            n = len(text)

            while i < n:
                if text[i : i + 2] == "{{":
                    end_pos = find_closing_brace(text, i + 2)
                    if end_pos != -1:
                        inner_content = text[i + 2 : end_pos]

                        color_key = chosen_color
                        if chosen_mode == "multi" and ":" in inner_content:
                            possible_color, rest = inner_content.split(":", 1)
                            if re.match(r"^[a-zA-Z0-9_-]+$", possible_color.strip()):
                                color_key = possible_color.strip().lower()
                                inner_content = rest

                        parse_nested_text(
                            inner_content, active_colors + [color_key], html_tokens
                        )
                        i = end_pos + 2
                        continue

                token_match = re.match(r"^(\w+)|([^\w\s]+|\s+)", text[i:])
                if token_match:
                    word_group, symbol_group = token_match.groups()
                    if word_group:
                        if active_colors:
                            target_colors[str(word_token_index)] = list(
                                set(active_colors)
                            )
                        html_tokens.append(
                            f'<span class="ts-word" data-idx="{word_token_index}">{html.escape(word_group)}</span>'
                        )
                        word_token_index += 1
                        i += len(word_group)
                    elif symbol_group:
                        if symbol_group.isspace():
                            html_tokens.append(
                                symbol_group.replace(
                                    " ", '<span class="ts-space"> </span>'
                                )
                            )
                        else:
                            html_tokens.append(html.escape(symbol_group))
                        i += len(symbol_group)
                else:
                    i += 1

        def find_closing_brace(text, start_idx):
            depth = 1
            idx = start_idx
            while idx < len(text) - 1:
                if text[idx : idx + 2] == "{{":
                    depth += 1
                    idx += 2
                elif text[idx : idx + 2] == "}}":
                    depth -= 1
                    if depth == 0:
                        return idx
                    idx += 2
                else:
                    idx += 1
            return -1

        for line in lines:
            line_tokens = []
            parse_nested_text(line, [], line_tokens)
            html_lines.append(f'<div class="ts-line">{"".join(line_tokens)}</div>')

        node["html_content"] = "".join(html_lines)
        node["target_json"] = json.dumps(target_colors)

        return [node]


def setup(app):
    app.add_node(textselect_node, html=(visit_textselect_html, depart_textselect_html))
    app.add_directive("textselect", TextSelectDirective)

    static_path = Path(__file__).parent / "_static"
    if str(static_path) not in app.config.html_static_path:
        app.config.html_static_path.append(str(static_path))

    app.add_js_file("textselect.js")
    app.add_css_file("textselect.css")

    return {
        "version": "1.5",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }