import html
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

# ============================================================
# Custom AST Nodes
# ============================================================


class StructuredQuestionNode(nodes.General, nodes.Element):
    pass


class StimulusNode(nodes.General, nodes.Element):
    pass


class SubQuestionNode(nodes.General, nodes.Element):
    pass


class ModelAnswerNode(nodes.General, nodes.Element):
    pass


class MarkingGuidanceNode(nodes.General, nodes.Element):
    pass


# ============================================================
# Directive Definitions
# ============================================================


class StructuredQuestionDirective(SphinxDirective):
    has_content = True
    required_arguments = 1
    final_argument_whitespace = True

    option_spec = {
        "total-marks": directives.positive_int,
        "category": directives.unchanged,
    }

    def run(self):
        node = StructuredQuestionNode()

        node["title"] = self.arguments[0]
        node["total_marks"] = self.options.get("total-marks", 0)
        node["category"] = self.options.get("category", "")

        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


class StimulusDirective(SphinxDirective):
    has_content = True

    def run(self):
        node = StimulusNode()

        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


class SubQuestionDirective(SphinxDirective):
    has_content = True
    required_arguments = 1
    final_argument_whitespace = True

    option_spec = {
        "marks": directives.positive_int,
    }

    def run(self):
        node = SubQuestionNode()

        node["title"] = self.arguments[0]
        node["marks"] = self.options.get("marks", 1)

        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


class ModelAnswerDirective(SphinxDirective):
    has_content = True

    def run(self):
        node = ModelAnswerNode()

        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


class MarkingGuidanceDirective(SphinxDirective):
    has_content = True

    def run(self):
        node = MarkingGuidanceNode()

        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


# ============================================================
# HTML Render Functions
# ============================================================


def visit_sq_node(self, node):
    title = html.escape(node["title"])
    category = html.escape(node["category"])

    category_badge = f'<span class="sq-category">{category}</span>' if category else ""

    self.body.append(
        f'<div class="sq-container" '
        f'data-total-marks="{node["total_marks"]}">'
        f'<div class="sq-header">'
        f'<div class="sq-title-group">'
        f'<h3 class="sq-title">{title}</h3>'
        f"{category_badge}"
        f"</div>"
        f'<div class="sq-score-tracker">'
        f"Marks: "
        f'<span class="sq-user-score">0</span>'
        f" / "
        f"<strong>{node['total_marks']}</strong>"
        f"</div>"
        f"</div>"
    )


def depart_sq_node(self, node):
    self.body.append("</div>")


# ============================================================
# Stimulus
# ============================================================


def visit_stimulus_node(self, node):
    self.body.append(
        '<div class="sq-stimulus">'
        '<div class="sq-stimulus-label">Scenario / Stimulus</div>'
    )


def depart_stimulus_node(self, node):
    self.body.append("</div>")


# ============================================================
# Sub-question
# ============================================================


def visit_subquestion_node(self, node):
    title = html.escape(node["title"])
    marks = node["marks"]

    mark_word = "mark" if marks == 1 else "marks"

    self.body.append(
        f'<div class="sq-subquestion" '
        f'data-marks="{marks}" '
        f'data-user-score="0">'
        f'<div class="sq-sub-header">'
        f'<span class="sq-sub-title">{title}</span>'
        f'<span class="sq-marks-tag">({marks} {mark_word})</span>'
        f"</div>"
        f'<div class="sq-sub-body">'
    )


def depart_subquestion_node(self, node):
    marks = node["marks"]

    score_pills = "".join(
        f'<button type="button" class="sq-score-btn" data-score="{m}" '
        f'aria-label="Give {m} out of {marks} marks">{m}</button>'
        for m in range(marks + 1)
    )

    self.body.append(
        # Close sq-sub-body
        "</div>"
        # Workspace
        '<div class="sq-workspace">'
        '<label class="sq-input-label">Your Response:</label>'
        '<textarea class="sq-textarea" placeholder="Type your answer here..."></textarea>'
        '<div class="sq-actions">'
        # Show / hide answer button
        '<button type="button" class="sq-btn sq-toggle-ans-btn" aria-expanded="false">'
        "Show Model Answer &amp; Self-Grading"
        "</button>"
        # Self grading
        '<div class="sq-self-grade hidden">'
        '<span class="sq-self-grade-label">Self Grade: </span>'
        f'<div class="sq-pill-group">{score_pills}</div>'
        "</div>"
        "</div>"
        # Close workspace
        "</div>"
        # Close sq-subquestion
        "</div>"
    )


# ============================================================
# Model Answer
# ============================================================


def visit_model_answer_node(self, node):
    self.body.append(
        '<div class="sq-answer-drawer hidden">'
        '<div class="sq-model-answer">'
        '<div class="sq-drawer-label">Model Answer</div>'
    )


def depart_model_answer_node(self, node):
    self.body.append("</div></div>")


# ============================================================
# Marking Guidance
# ============================================================


def visit_marking_guidance_node(self, node):
    self.body.append(
        '<div class="sq-answer-drawer hidden">'
        '<div class="sq-marking-guidance">'
        '<div class="sq-drawer-label">Marking Guidance</div>'
    )


def depart_marking_guidance_node(self, node):
    self.body.append("</div></div>")


# ============================================================
# Extension Setup
# ============================================================


def setup(app):
    app.add_node(StructuredQuestionNode, html=(visit_sq_node, depart_sq_node))
    app.add_node(StimulusNode, html=(visit_stimulus_node, depart_stimulus_node))
    app.add_node(SubQuestionNode, html=(visit_subquestion_node, depart_subquestion_node))
    app.add_node(ModelAnswerNode, html=(visit_model_answer_node, depart_model_answer_node))
    app.add_node(MarkingGuidanceNode, html=(visit_marking_guidance_node, depart_marking_guidance_node))

    static_path = Path(__file__).parent / "_static"
    if str(static_path) not in app.config.html_static_path:
        app.config.html_static_path.append(str(static_path))

    app.add_directive("structuredquestion", StructuredQuestionDirective)
    app.add_directive("stimulus", StimulusDirective)
    app.add_directive("subquestion", SubQuestionDirective)
    app.add_directive("model-answer", ModelAnswerDirective)
    app.add_directive("marking-guidance", MarkingGuidanceDirective)

    app.add_css_file("structuredquestion.css")
    app.add_js_file("structuredquestion.js")

    return {
        "version": "1.2",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }