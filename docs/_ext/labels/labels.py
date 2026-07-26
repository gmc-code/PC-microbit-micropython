import html
import random
import os
import shutil
import logging
from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

logger = logging.getLogger(__name__)

class label_node(nodes.General, nodes.Element):
    pass

def visit_label_html(self, node):
    self.body.append('<div class="label-interactive-block">')

def depart_label_html(self, node):
    self.body.append('</div>')


class LabelDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True

    option_spec = {
        'image': directives.unchanged,
        'width': directives.positive_int,
        'height': directives.positive_int,
        'font-size': directives.unchanged,  # Accepts values like "0.85rem", "14px", "1.2rem"
    }

    def run(self):
        env = self.env

        if not hasattr(env, "label_images"):
            env.label_images = {}

        img_rel = self.options.get('image', '')
        if not img_rel and self.arguments:
            arg = self.arguments[0].strip()
            if not arg.startswith(':') and not arg.startswith('*'):
                img_rel = arg

        rel_img_path = ""
        if img_rel:
            _, img_full_path = env.relfn2path(img_rel, env.docname)
            img_path_obj = Path(img_full_path)

            if img_path_obj.exists():
                image_filename = img_path_obj.name
                env.label_images[str(img_path_obj)] = image_filename

                doc_path = Path(env.docname)
                depth = len(doc_path.parents) - 1 if str(
                    doc_path.parent) != '.' else 0
                rel_prefix = "../" * depth if depth > 0 else ""
                rel_img_path = f"{rel_prefix}_images/{image_filename}"
            else:
                rel_img_path = Path(img_rel).as_posix()

        width = self.options.get('width', 560)
        height = self.options.get('height', 500)

        # Default font size if none specified in RST
        font_size = self.options.get('font-size', '0.95rem')

        labels_data = []
        for line in self.content:
            line_str = line.strip()
            if not line_str:
                continue

            cleaned_line = line_str.lstrip('*- ').strip()

            if 'label:' in cleaned_line:
                lbl = cleaned_line.split('label:', 1)[1].strip()
                labels_data.append({
                    'label': lbl,
                    'pos': [0, 0, 0, 0],
                    'align': 'left'
                })
            elif 'pos:' in cleaned_line and labels_data:
                coords_str = cleaned_line.split('pos:', 1)[1].strip()
                coords = [
                    int(c.strip()) for c in coords_str.split(',')
                    if c.strip().lstrip('-').isdigit()
                ]
                if len(coords) >= 4:
                    labels_data[-1]['pos'] = coords[:4]
            elif 'align:' in cleaned_line and labels_data:
                align_str = cleaned_line.split('align:', 1)[1].strip()
                labels_data[-1]['align'] = align_str

        if not labels_data:
            logger.warning(
                f"[label-diagram] No labels parsed in document: {env.docname}")

        labels = [d['label'] for d in labels_data]

        # Pass the font size as a CSS variable on the main container
        html_out = f'<div class="label-activity-container" style="--label-font-size: {font_size};">'

        # Sort labels A to Z
        sorted_labels = sorted(labels, key=lambda s: s.lower())

        # Determine line count variant class based on total number/length of labels
        num_items = len(sorted_labels)
        if num_items <= 6:
            line_class = "lines-1"
        elif num_items <= 12:
            line_class = "lines-2"
        elif num_items <= 16:
            line_class = "lines-3"
        else:
            line_class = "lines-4"

        # Word Bank Tray with dynamic line variant class
        html_out += f'<div class="label-wordbank-tray {line_class}" data-role="bank">'
        for idx, label in enumerate(sorted_labels):
            clean_label = html.escape(label)
            html_out += f'<div class="label-draggable" draggable="true" id="drag-{idx}" data-word="{clean_label}">{clean_label}</div>'
        html_out += '</div>'

        # Canvas
        canvas_style = f"position: relative; width: {width}px; height: {height}px; background-size: cover; background-position: center; background-repeat: no-repeat;"
        if rel_img_path:
            canvas_style += f" background-image: url('{rel_img_path}');"

        html_out += f'<div class="label-diagram-canvas" style="{canvas_style}">'

        # Drop Zones
        for idx, item in enumerate(labels_data):
            x1, y1, x2, y2 = item['pos']
            correct_word = html.escape(item['label'])
            align_val = html.escape(item['align'])
            letter_prefix = chr(
                65 + (idx % 26)
            ) if idx < 26 else f"{chr(65 + (idx // 26) - 1)}{chr(65 + (idx % 26))}"

            w = max(abs(x2 - x1), 40)
            h = max(abs(y2 - y1), 20)

            # Alignment anchors
            right_pos = width - x2
            x_center = (x1 + x2) // 2  # True horizontal midpoint

            style = (f"position: absolute; "
                     f"top: {y1}px; "
                     f"height: {h}px; "
                     f"--left-pos: {x1}px; "
                     f"--right-pos: {right_pos}px; "
                     f"--center-pos: {x_center}px; "
                     f"--min-w: {w}px;")

            html_out += (f'<div class="label-dropzone" style="{style}" '
                         f'data-correct="{correct_word}" '
                         f'data-prefix="{letter_prefix}." '
                         f'data-align="{align_val}"></div>')
        html_out += '</div>'

        # Controls
        html_out += '''
        <div class="label-controls">
            <button class="label-btn label-btn-check" type="button" onclick="scoreLabels(this)">Check Answers</button>
            <button class="label-btn label-btn-reference" type="button" onclick="toggleReferenceMode(this)">A,B,C Mode</button>
            <button class="label-btn label-btn-answers" type="button" onclick="showAnswers(this)">Show Answers</button>
            <button class="label-btn label-btn-reset" type="button" onclick="resetLabels(this)">Reset</button>
            <span class="label-score-display"></span>
        </div>
        </div>
        '''

        node = label_node()
        node += nodes.raw("", html_out, format="html")
        return [node]

def copy_label_images(app, exception):
    if exception:
        return

    env = app.builder.env
    if not hasattr(env, "label_images"):
        return

    outdir = Path(app.builder.outdir)
    images_dir = outdir / "_images"
    images_dir.mkdir(parents=True, exist_ok=True)

    for src, name in env.label_images.items():
        src = Path(src)
        if not src.exists():
            logger.warning(f"Label image not found: {src}")
            continue
        dst = images_dir / name
        shutil.copy2(src, dst)

def setup(app):
    app.add_node(label_node, html=(visit_label_html, depart_label_html))
    app.add_directive("label-diagram", LabelDirective)
    app.connect("build-finished", copy_label_images)

    static_path = Path(__file__).parent / "_static"
    if static_path.exists():
        if str(static_path) not in app.config.html_static_path:
            app.config.html_static_path.append(str(static_path))

    app.add_js_file("labels.js")
    app.add_css_file("labels.css")

    return {
        "version": "8.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True
    }