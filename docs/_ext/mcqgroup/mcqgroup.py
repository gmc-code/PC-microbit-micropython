from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class mcqgroup_node(nodes.General, nodes.Element):
    pass


def render_nav_bar():
    return (
        '    <div class="mcqgroup-nav-bar">\n'
        '      <div class="mcqgroup-nav-left">\n'
        '        <button class="mcqgroup-btn-first" type="button" title="First Question">&laquo; First</button>\n'
        '        <button class="mcqgroup-btn-prev" type="button" title="Previous Question">&lsaquo; Prev</button>\n'
        '      </div>\n'
        '      <span class="mcqgroup-nav-status">Question <span class="mcqgroup-current-idx">1</span> of <span class="mcqgroup-total-idx">0</span></span>\n'
        '      <div class="mcqgroup-nav-right">\n'
        '        <button class="mcqgroup-btn-next" type="button" title="Next Question">Next &rsaquo;</button>\n'
        '        <button class="mcqgroup-btn-last" type="button" title="Last Question">Last &raquo;</button>\n'
        '      </div>\n'
        '    </div>\n'
    )


def visit_mcqgroup_html(self, node):
    show_instant = node.get("show_instant_feedback", False)
    enable_instant = node.get("enable_instant_feedback", False)
    shuffle_q = node.get("shuffle_questions", False)
    num_q = node.get("num_questions", None)
    nav_pos = node.get("nav_position", "bottom")

    data_attrs = 'data-view-mode="wizard"'
    data_attrs += f' data-nav-position="{nav_pos}"'
    if shuffle_q:
        data_attrs += ' data-shuffle-questions="true"'
    if num_q is not None:
        data_attrs += f' data-num-questions="{num_q}"'

    self.body.append(f'<div class="mcqgroup-block" {data_attrs}>')
    self.body.append('  <div class="mcqgroup-header">')
    self.body.append('    <div class="mcqgroup-top-row">')
    self.body.append('      <div class="mcqgroup-progress-container">')
    self.body.append('        <div class="mcqgroup-progress-text">Progress: <span class="mcqgroup-progress-count">0</span></div>')
    self.body.append('        <div class="mcqgroup-progress-bar-bg"><div class="mcqgroup-progress-bar-fill" style="width: 0%;"></div></div>')
    self.body.append('      </div>')
    self.body.append('      <div class="mcqgroup-header-right">')
    self.body.append('        <div class="mcqgroup-score-badge">Score: <span class="mcqgroup-score-value">0</span> / <span class="mcqgroup-total-value">0</span></div>')
    self.body.append('        <button class="mcqgroup-btn-toggle" type="button">All Q Mode</button>')
    self.body.append('      </div>')
    self.body.append('    </div>')
    self.body.append('    <div class="mcqgroup-action-bar">')
    self.body.append('      <button class="mcqgroup-btn-start" type="button">Start Quiz</button>')
    self.body.append('      <button class="mcqgroup-btn-check" type="button">Check Group Answers</button>')
    self.body.append('      <label class="mcqgroup-feedback-label"><input type="checkbox" class="mcqgroup-show-feedback" /> Show Feedback</label>')
    self.body.append('      <button class="mcqgroup-btn-reset" type="button">Reset Group</button>')

    if show_instant:
        checked_attr = ' checked="checked"' if enable_instant else ''
        self.body.append(f'      <label class="mcqgroup-feedback-label"><input type="checkbox" class="mcqgroup-instant-feedback"{checked_attr} /> Instant Feedback</label>')

    self.body.append('    </div>')

    # Render Nav Bar at top if specified
    if nav_pos in ("top", "both"):
        self.body.append(render_nav_bar())

    self.body.append('  </div>')
    self.body.append('  <div class="mcqgroup-questions-container">')


def depart_mcqgroup_html(self, node):
    nav_pos = node.get("nav_position", "bottom")
    self.body.append('  </div>')

    # Render Nav Bar at bottom if specified
    if nav_pos in ("bottom", "both"):
        self.body.append(render_nav_bar())

    # Compact Bottom Toolbar for "All Q Mode"
    self.body.append('  <div class="mcqgroup-bottom-bar" style="display: none;">')
    self.body.append('    <button class="mcqgroup-btn-scroll-top" type="button" title="Scroll to Top">&uarr; Back to Top</button>')
    self.body.append('  </div>')
    self.body.append('</div>')


class MCQGroupDirective(SphinxDirective):
    has_content = True
    option_spec = {
        "show_instant_feedback": directives.flag,
        "show-instant-feedback": directives.flag,
        "enable_instant_feedback": directives.flag,
        "enable-instant-feedback": directives.flag,
        "shuffle_questions": directives.flag,
        "shuffle-questions": directives.flag,
        "num_questions": directives.positive_int,
        "num-questions": directives.positive_int,
        "nav_position": lambda arg: directives.choice(arg, ("top", "bottom", "both")),
        "nav-position": lambda arg: directives.choice(arg, ("top", "bottom", "both")),
    }

    def run(self):
        node = mcqgroup_node()
        enable_instant = "enable_instant_feedback" in self.options or "enable-instant-feedback" in self.options
        show_instant = "show_instant_feedback" in self.options or "show-instant-feedback" in self.options or enable_instant
        shuffle_q = "shuffle_questions" in self.options or "shuffle-questions" in self.options
        num_q = self.options.get("num_questions", self.options.get("num-questions", None))
        nav_pos = self.options.get("nav_position", self.options.get("nav-position", "bottom"))

        node["show_instant_feedback"] = show_instant
        node["enable_instant_feedback"] = enable_instant
        node["shuffle_questions"] = shuffle_q
        node["num_questions"] = num_q
        node["nav_position"] = nav_pos

        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def setup(app):
    app.add_node(mcqgroup_node, html=(visit_mcqgroup_html, depart_mcqgroup_html))

    app.add_directive("mcqgroup", MCQGroupDirective)
    app.add_directive("multichoicegroup", MCQGroupDirective)

    static_path = Path(__file__).parent / "_static"
    if str(static_path) not in app.config.html_static_path:
        app.config.html_static_path.append(str(static_path))

    app.add_js_file("mcqgroup.js")
    app.add_css_file("mcqgroup.css")

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }