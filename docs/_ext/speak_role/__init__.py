from pathlib import Path
from docutils import nodes


def speak_role_fn(
    name,
    rawtext,
    text,
    lineno,
    inliner,
    options=None,
    content=None
):
    """
    Inline role:

        :speak:`text to be spoken`

    or:

        :speak:`display text <text to speak>`
    """

    if options is None:
        options = {}

    # Handle:
    # :speak:`display text <text to speak>`
    if '<' in text and text.endswith('>'):
        display_text, spoken_text = text[:-1].split('<', 1)
        display_text = display_text.strip()
        spoken_text = spoken_text.strip()
    else:
        display_text = text.strip()
        spoken_text = text.strip()

    # Escape values before putting them into HTML attributes.
    import html

    display_text_html = html.escape(display_text)
    spoken_text_html = html.escape(spoken_text, quote=True)

    html_content = (
        '<span class="speak-container">'
        f'<button type="button" '
        f'class="speak-btn" '
        f'data-speak-text="{spoken_text_html}" '
        f'title="Listen">'
        '🔊'
        '</button> '
        f'<span class="speak-text">{display_text_html}</span>'
        '</span>'
    )

    node = nodes.raw('', html_content, format='html')

    return [node], []


def setup(app):
    """Sphinx extension initialization."""

    # Register the role.
    app.add_role('speak', speak_role_fn)

    # The actual directory is:
    #
    # docs/_ext/speak_role/_static/
    #
    static_dir = Path(__file__).parent / '_static'

    # Make the extension's static files available to Sphinx.
    static_str = str(static_dir.resolve())

    if static_str not in app.config.html_static_path:
        app.config.html_static_path.append(static_str)

    # Register the assets.
    app.add_css_file('speak.css')
    app.add_js_file('speak.js')

    return {
        'version': '0.1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }