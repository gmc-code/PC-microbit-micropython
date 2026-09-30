import html
import random
import re
from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class wordjumble_node(nodes.General, nodes.Element):
    pass


def visit_wordjumble_html(self, node):
    chosen_theme = node.get("theme", "")
    chosen_color = node.get("color", "blue")
    chosen_style = node.get("style", "filled")

    theme_class = f"theme-{chosen_theme}" if chosen_theme else ""
    color_class = f"wj-color-{chosen_color}"
    style_class = f"wj-style-{chosen_style}"

    classes = " ".join(
        filter(None, ["wordjumble-block", theme_class, color_class, style_class])
    )

    self.body.append(f'<div class="{classes}">')
    self.body.append(
        f'<div class="wordjumble-instructions">{node.get("instructions", "")}</div>'
    )
    self.body.append('<div class="wordjumble-content">')
    self.body.append(node.get("html_content", ""))
    self.body.append("</div></div>")
    raise nodes.SkipNode


def depart_wordjumble_html(self, node):
    pass


class WordJumbleDirective(SphinxDirective):
    has_content = True

    option_spec = {
        "letters": directives.nonnegative_int,
        "keep-first": directives.flag,
        "keep-first-two": directives.flag,  # New flag to lock the first 2 letters
        "keep-last": directives.flag,
        "shuffle": directives.unchanged,  # Accepts: 'random' (default) or 'alpha'/'a-z'
        "theme": directives.unchanged,
        "instructions": directives.unchanged,
        "color": directives.unchanged,
        "style": directives.unchanged,
    }

    def _jumble_word(self, word, num_letters, keep_first, keep_first_two, keep_last, shuffle_mode):
        length = len(word)
        if length <= 1:
            return word

        # Set starting index based on keep-first-two or keep-first flags
        if keep_first_two:
            start_idx = 2 if length >= 3 else 1
        elif keep_first:
            start_idx = 1
        else:
            start_idx = 0

        end_idx = length - 1 if keep_last else length
        middle_indices = list(range(start_idx, end_idx))

        # Check if constraints force picking identical characters
        chars = list(word)
        if (keep_first or keep_first_two) and keep_last and len(middle_indices) >= 2:
            unique_chars = set(chars[i] for i in middle_indices)
            if len(unique_chars) <= 1:
                # Ignore keep_last to expand character pool
                end_idx = length
                middle_indices = list(range(start_idx, end_idx))

        if len(middle_indices) < 2:
            return word

        # Determine count of letters to scramble (minimum 2)
        if num_letters is not None and num_letters > 0:
            count = max(2, min(num_letters, len(middle_indices)))
        else:
            count = len(middle_indices)

        # Select swap indices, ensuring selected characters are not all identical
        swap_indices = None
        max_index_selection_attempts = 20

        for _ in range(max_index_selection_attempts):
            candidate_indices = random.sample(middle_indices, count)
            selected_chars = [chars[i] for i in candidate_indices]

            if len(set(selected_chars)) > 1:
                swap_indices = candidate_indices
                break

        # Fallback: Ignore keep-last if distinct characters could not be found
        if swap_indices is None and keep_last:
            middle_indices = list(range(start_idx, length))
            count = max(2, min(count, len(middle_indices)))
            for _ in range(max_index_selection_attempts):
                candidate_indices = random.sample(middle_indices, count)
                selected_chars = [chars[i] for i in candidate_indices]
                if len(set(selected_chars)) > 1:
                    swap_indices = candidate_indices
                    break

        if swap_indices is None:
            swap_indices = middle_indices
            if len(set(chars[i] for i in swap_indices)) <= 1:
                return word

        jumbled_result = word

        # 1. Mode 1: Alphabetical (A-Z) Sorting
        if shuffle_mode in ["alpha", "a-z", "alphabetical"]:
            sorted_chars = sorted([chars[i] for i in swap_indices], key=lambda c: c.lower())
            temp_chars = list(chars)
            for i, original_idx in enumerate(swap_indices):
                temp_chars[original_idx] = sorted_chars[i]
            res = "".join(temp_chars)

            if res == word:
                sorted_chars.reverse()
                for i, original_idx in enumerate(swap_indices):
                    temp_chars[original_idx] = sorted_chars[i]
                res = "".join(temp_chars)

            jumbled_result = res

        # 2. Mode 2: Standard Random Shuffle
        else:
            shuffled_chars = [chars[i] for i in swap_indices]
            random.shuffle(shuffled_chars)
            temp_chars = list(chars)
            for i, original_idx in enumerate(swap_indices):
                temp_chars[original_idx] = shuffled_chars[i]
            jumbled_result = "".join(temp_chars)

        # 3. Final Safety Check: Repeated random shuffle loop until jumbled_result != word
        shuffle_attempts = 0
        max_shuffle_attempts = 50

        while jumbled_result == word and shuffle_attempts < max_shuffle_attempts:
            shuffled_chars = [chars[i] for i in swap_indices]
            random.shuffle(shuffled_chars)
            temp_chars = list(chars)
            for i, original_idx in enumerate(swap_indices):
                temp_chars[original_idx] = shuffled_chars[i]
            jumbled_result = "".join(temp_chars)
            shuffle_attempts += 1

        # Fallback if random repeated shuffles fail
        if jumbled_result == word:
            sorted_chars = sorted([chars[i] for i in swap_indices], key=lambda c: c.lower())
            if "".join(sorted_chars) == "".join(chars[i] for i in swap_indices):
                sorted_chars.reverse()
            temp_chars = list(chars)
            for i, original_idx in enumerate(swap_indices):
                temp_chars[original_idx] = sorted_chars[i]
            jumbled_result = "".join(temp_chars)

        return jumbled_result

    def run(self):
        full_text = "\n".join(self.content)
        node = wordjumble_node()

        num_letters = self.options.get("letters", None)
        keep_first = "keep-first" in self.options
        keep_first_two = "keep-first-two" in self.options
        keep_last = "keep-last" in self.options
        shuffle_mode = self.options.get("shuffle", "random").strip().lower()

        # 1. Themes
        chosen_theme = self.options.get("theme", "white").strip().lower()
        if chosen_theme not in ["white", "light"]:
            chosen_theme = "white"
        node["theme"] = chosen_theme

        # 2. Colors
        chosen_color = self.options.get("color", "blue").strip().lower()
        valid_colors = [
            "red", "participant", "green", "process", "blue", "circumstance",
            "conj", "part", "theme", "rheme", "dependent", "embedded",
            "relative", "projected",
        ]
        if chosen_color not in valid_colors:
            chosen_color = "blue"
        node["color"] = chosen_color

        # 3. Styles
        chosen_style = self.options.get("style", "filled").strip().lower()
        if chosen_style not in ["plain", "border", "filled"]:
            chosen_style = "filled"
        node["style"] = chosen_style

        node["instructions"] = html.escape(
            self.options.get(
                "instructions",
                "Unjumble each word by typing the correct spelling in the box next to it.",
            )
        )

        token_pattern = re.compile(r"(\w+)|([^\w\s]+|\s+)")
        html_tokens = []

        for match in token_pattern.finditer(full_text):
            word_group, symbol_group = match.groups()

            if word_group:
                jumbled = self._jumble_word(
                    word_group, num_letters, keep_first, keep_first_two, keep_last, shuffle_mode
                )
                escaped_orig = html.escape(word_group)
                escaped_jumbled = html.escape(jumbled)

                item_html = (
                    f'<span class="wj-item">'
                    f'<span class="wj-word">{escaped_jumbled}</span>'
                    f'<input type="text" class="wj-input" data-answer="{escaped_orig}" '
                    f'autocomplete="off" spellcheck="false" />'
                    f'</span>'
                )
                html_tokens.append(item_html)
            elif symbol_group:
                if symbol_group.isspace():
                    html_tokens.append(
                        symbol_group.replace("\n", "<br>").replace(
                            " ", '<span class="wj-space"> </span>'
                        )
                    )
                else:
                    html_tokens.append(html.escape(symbol_group))

        node["html_content"] = "".join(html_tokens)
        return [node]


def setup(app):
    app.add_node(wordjumble_node, html=(visit_wordjumble_html, depart_wordjumble_html))
    app.add_directive("wordjumble", WordJumbleDirective)

    static_path = Path(__file__).parent / "_static"
    if str(static_path) not in app.config.html_static_path:
        app.config.html_static_path.append(str(static_path))

    app.add_js_file("wordjumble.js")
    app.add_css_file("wordjumble.css")

    return {
        "version": "1.4",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }