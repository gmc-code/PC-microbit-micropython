from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class clozegroup_node(nodes.General, nodes.Element):
    pass


def render_nav_bar():
    return (
        '    <div class="clozegroup-nav-bar">\n'
        '      <div class="clozegroup-nav-left">\n'
        '        <button class="clozegroup-btn-first" type="button" title="First Question">&laquo; First</button>\n'
        '        <button class="clozegroup-btn-prev" type="button" title="Previous Question">&lsaquo; Prev</button>\n'
        '      </div>\n'
        '      <span class="clozegroup-nav-status">Question <span class="clozegroup-current-idx">1</span> of <span class="clozegroup-total-idx">0</span></span>\n'
        '      <div class="clozegroup-nav-right">\n'
        '        <button class="clozegroup-btn-next" type="button" title="Next Question">Next &rsaquo;</button>\n'
        '        <button class="clozegroup-btn-last" type="button" title="Last Question">Last &raquo;</button>\n'
        '      </div>\n'
        '    </div>\n'
    )


def visit_clozegroup_html(self, node):
    shuffle_q = node.get("shuffle_questions", False)
    num_q = node.get("num_questions", None)
    nav_pos = node.get("nav_position", "bottom")
    show_instant = node.get("show_instant_feedback", False)
    enable_instant = node.get("enable_instant_feedback", False)

    data_attrs = 'data-view-mode="wizard"'
    data_attrs += f' data-nav-position="{nav_pos}"'
    if shuffle_q:
        data_attrs += ' data-shuffle-questions="true"'
    if num_q is not None:
        data_attrs += f' data-num-questions="{num_q}"'
    if show_instant:
        data_attrs += ' data-show-instant-feedback="true"'
    if enable_instant:
        data_attrs += ' data-enable-instant-feedback="true"'

    self.body.append(f'<div class="clozegroup-block" {data_attrs}>')
    self.body.append('  <div class="clozegroup-header">')
    self.body.append('    <div class="clozegroup-top-row">')
    self.body.append('      <div class="clozegroup-progress-container">')
    self.body.append('        <div class="clozegroup-progress-text">Progress: <span class="clozegroup-progress-count">0%</span></div>')
    self.body.append('        <div class="clozegroup-progress-bar-bg"><div class="clozegroup-progress-bar-fill" style="width: 0%;"></div></div>')
    self.body.append('      </div>')
    self.body.append('      <div class="clozegroup-header-right">')
    self.body.append('        <div class="clozegroup-score-badge">Gaps Correct: <span class="clozegroup-score-value">0</span> / <span class="clozegroup-total-value">0</span></div>')
    self.body.append('        <button class="clozegroup-btn-toggle" type="button">All Q Mode</button>')
    self.body.append('      </div>')
    self.body.append('    </div>')
    self.body.append('    <div class="clozegroup-action-bar">')
    self.body.append('      <button class="clozegroup-btn-start" type="button">Start Cloze Test</button>')
    self.body.append('      <button class="clozegroup-btn-check" type="button">Check Group Answers</button>')
    self.body.append('      <button class="clozegroup-btn-reset" type="button">Reset Group</button>')

    # Render Instant Feedback checkbox to the right of the Reset button
    if show_instant:
        checked_attr = ' checked' if enable_instant else ''
        self.body.append('      <label class="clozegroup-toggle-label">')
        self.body.append(f'        <input type="checkbox" class="clozegroup-toggle-instant-feedback"{checked_attr}> Instant Feedback')
        self.body.append('      </label>')

    self.body.append('    </div>')

    if nav_pos in ("top", "both"):
        self.body.append(render_nav_bar())

    self.body.append('  </div>')
    self.body.append('  <div class="clozegroup-questions-container">')


def depart_clozegroup_html(self, node):
    nav_pos = node.get("nav_position", "bottom")
    self.body.append('  </div>')

    if nav_pos in ("bottom", "both"):
        self.body.append(render_nav_bar())

    self.body.append('  <div class="clozegroup-bottom-bar" style="display: none;">')
    self.body.append('    <button class="clozegroup-btn-scroll-top" type="button" title="Scroll to Top">&uarr; Back to Top</button>')
    self.body.append('  </div>')
    self.body.append('</div>')


class ClozeGroupDirective(SphinxDirective):
    has_content = True
    option_spec = {
        "shuffle_questions": directives.flag,
        "shuffle-questions": directives.flag,
        "num_questions": directives.positive_int,
        "num-questions": directives.positive_int,
        "nav_position": lambda arg: directives.choice(arg, ("top", "bottom", "both")),
        "nav-position": lambda arg: directives.choice(arg, ("top", "bottom", "both")),
        "show_instant_feedback": directives.flag,
        "show-instant-feedback": directives.flag,
        "enable_instant_feedback": directives.flag,
        "enable-instant-feedback": directives.flag,
    }

    def run(self):
        node = clozegroup_node()
        shuffle_q = "shuffle_questions" in self.options or "shuffle-questions" in self.options
        num_q = self.options.get("num_questions", self.options.get("num-questions", None))
        nav_pos = self.options.get("nav_position", self.options.get("nav-position", "bottom"))
        show_instant_f = "show_instant_feedback" in self.options or "show-instant-feedback" in self.options
        enable_instant_f = "enable_instant_feedback" in self.options or "enable-instant-feedback" in self.options

        node["shuffle_questions"] = shuffle_q
        node["num_questions"] = num_q
        node["nav_position"] = nav_pos
        node["show_instant_feedback"] = show_instant_f
        node["enable_instant_feedback"] = enable_instant_f

        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def setup(app):
    app.add_node(clozegroup_node, html=(visit_clozegroup_html, depart_clozegroup_html))
    app.add_directive("clozegroup", ClozeGroupDirective)

    static_path = Path(__file__).parent / "_static"
    if str(static_path) not in app.config.html_static_path:
        app.config.html_static_path.append(str(static_path))

    app.add_js_file("clozegroup.js")
    app.add_css_file("clozegroup.css")

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }