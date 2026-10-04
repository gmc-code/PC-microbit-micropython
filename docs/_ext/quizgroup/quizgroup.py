from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class quizgroup_node(nodes.General, nodes.Element):
    pass


def render_nav_bar():
    return (
        '    <div class="quizgroup-nav-bar">\n'
        '      <div class="quizgroup-nav-left">\n'
        '        <button class="quizgroup-btn-first" type="button" title="First Question">&laquo; First</button>\n'
        '        <button class="quizgroup-btn-prev" type="button" title="Previous Question">&lsaquo; Prev</button>\n'
        '      </div>\n'
        '      <span class="quizgroup-nav-status">Question <span class="quizgroup-current-idx">1</span> of <span class="quizgroup-total-idx">0</span></span>\n'
        '      <div class="quizgroup-nav-right">\n'
        '        <button class="quizgroup-btn-next" type="button" title="Next Question">Next &rsaquo;</button>\n'
        '        <button class="quizgroup-btn-last" type="button" title="Last Question">Last &raquo;</button>\n'
        '      </div>\n'
        '    </div>\n'
    )


def visit_quizgroup_html(self, node):
    shuffle_q = node.get("shuffle_questions", False)
    num_q = node.get("num_questions", None)
    nav_pos = node.get("nav_position", "bottom")
    show_feedback = node.get("show_instant_feedback", False)
    enable_feedback = node.get("enable_instant_feedback", False)

    data_attrs = 'data-view-mode="wizard"'
    data_attrs += f' data-nav-position="{nav_pos}"'
    if shuffle_q:
        data_attrs += ' data-shuffle-questions="true"'
    if num_q is not None:
        data_attrs += f' data-num-questions="{num_q}"'
    if show_feedback:
        data_attrs += ' data-show-instant-feedback="true"'
    if enable_feedback:
        data_attrs += ' data-enable-instant-feedback="true"'

    self.body.append(f'<div class="quizgroup-block" {data_attrs}>')
    self.body.append('  <div class="quizgroup-header">')
    self.body.append('    <div class="quizgroup-top-row">')
    self.body.append('      <div class="quizgroup-progress-container">')
    self.body.append('        <div class="quizgroup-progress-text">Progress: <span class="quizgroup-progress-count">0%</span></div>')
    self.body.append('        <div class="quizgroup-progress-bar-bg"><div class="quizgroup-progress-bar-fill" style="width: 0%;"></div></div>')
    self.body.append('      </div>')
    self.body.append('      <div class="quizgroup-header-right">')
    self.body.append('        <div class="quizgroup-score-badge">Score: <span class="quizgroup-score-value">0</span> / <span class="quizgroup-total-value">0</span></div>')
    self.body.append('        <button class="quizgroup-btn-toggle" type="button">All Q Mode</button>')
    self.body.append('      </div>')
    self.body.append('    </div>')
    self.body.append('    <div class="quizgroup-action-bar">')
    self.body.append('      <button class="quizgroup-btn-start" type="button">Start Quiz</button>')
    self.body.append('      <button class="quizgroup-btn-check" type="button">Check Quiz Answers</button>')
    self.body.append('      <button class="quizgroup-btn-reset" type="button">Reset Quiz</button>')

    # Conditional render for instant feedback checkbox control
    if show_feedback:
        checked_attr = ' checked="checked"' if enable_feedback else ''
        self.body.append('      <label class="quizgroup-instant-feedback-label">')
        self.body.append(f'        <input type="checkbox" class="quizgroup-toggle-instant-feedback"{checked_attr}> Instant Feedback')
        self.body.append('      </label>')

    self.body.append('    </div>')

    if nav_pos in ("top", "both"):
        self.body.append(render_nav_bar())

    self.body.append('  </div>')
    self.body.append('  <div class="quizgroup-questions-container">')


def depart_quizgroup_html(self, node):
    nav_pos = node.get("nav_position", "bottom")
    self.body.append('  </div>')

    if nav_pos in ("bottom", "both"):
        self.body.append(render_nav_bar())

    self.body.append('  <div class="quizgroup-bottom-bar" style="display: none;">')
    self.body.append('    <button class="quizgroup-btn-scroll-top" type="button" title="Scroll to Top">&uarr; Back to Top</button>')
    self.body.append('  </div>')
    self.body.append('</div>')


class QuizGroupDirective(SphinxDirective):
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
        node = quizgroup_node()
        shuffle_q = "shuffle_questions" in self.options or "shuffle-questions" in self.options
        num_q = self.options.get("num_questions", self.options.get("num-questions", None))
        nav_pos = self.options.get("nav_position", self.options.get("nav-position", "bottom"))
        enable_feedback = "enable_instant_feedback" in self.options or "enable-instant-feedback" in self.options
        show_feedback = "show_instant_feedback" in self.options or "show-instant-feedback" in self.options or enable_feedback

        node["shuffle_questions"] = shuffle_q
        node["num_questions"] = num_q
        node["nav_position"] = nav_pos
        node["show_instant_feedback"] = show_feedback
        node["enable_instant_feedback"] = enable_feedback

        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def setup(app):
    app.add_node(quizgroup_node, html=(visit_quizgroup_html, depart_quizgroup_html))
    app.add_directive("quizgroup", QuizGroupDirective)

    static_path = Path(__file__).parent / "_static"
    if str(static_path) not in app.config.html_static_path:
        app.config.html_static_path.append(str(static_path))

    app.add_js_file("quizgroup.js")
    app.add_css_file("quizgroup.css")

    return {
        "version": "1.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }