# Configuration file for the Sphinx documentation builder.
# see https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

import sphinx_rtd_theme
project = 'PC-Microbit'
copyright = '2021-26, GMC'
author = 'GMC'


# -- General configuration ---------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx_copybutton',
    'sphinx.ext.todo',
    'sphinx.ext.autodoc',
    'sphinx_togglebutton',
    'sphinx_design',
    "sphinx_new_tab_link",
]


# for copybutton to allow use of :class: no-copybutton  in code blocks
# copybutton_selector = "div:not(.no-copybutton) > div.highlight > pre"

# for sphinx_new_tab_link  False si default
# new_tab_link_show_external_link_icon = False


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# if using To Dos and want them to showup
todo_include_todos = True

# default python Pygments (syntax highlighting) style to use.
# for other styles see https://pygments.org/docs/lexers/#lexers-for-python-and-related-languages
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------

# The theme to use for HTML and HTML Help pages.
# See the documentation for a list of builtin themes.

html_theme = 'sphinx_rtd_theme'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None
html_title = "PC-Microbit-Micropython"

# Use custom css
html_css_files = ["css/custom.css"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# html_static_path = ['../_static/'] # for jupyter

# -- sphinx-rtd-theme Theme Options ------
# See: https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html

html_theme_options = {
    'logo_only': False,  # False so text is shown
    'prev_next_buttons_location': 'both',  # Can be bottom, top, both , or None
    'style_external_links': True,  # True to Add an icon next to external links
    # 'style_nav_header_background': 'blue',
    'style_nav_header_background': 'linear-gradient(to right, blueviolet 15%, limegreen 50%, royalblue 80%)',
    # Toc options;
    'collapse_navigation': True,  # False so nav entries have the [+] icons
    'sticky_navigation': False,  # True so the nav scrolls with main page
    'navigation_depth': 2,  # -1 for no limit, slow to build
    'includehidden': False,  # displays toctree that are hidden
    'titles_only': False  # False so page subheadings are in the nav.
}

# -- RTDs logos -------------------------------
html_favicon = "_static/favicon.ico"
html_logo = "_static/logo_navyblue.png"


# -- Options for LaTeX output ------------------------------
# see https://sphinxguide.readthedocs.io/en/latest/sphinx_basics/settings.html for latex code

latex_engine = 'xelatex'  # xelatex is better than pdflatex for unicode
latex_elements = {
    # to use latex dvipsnames and svgcolour names if so desired
    'passoptionstopackages': r'\PassOptionsToPackage{dvipsnames*,svgnames}{xcolor}',
    #
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',
    #
    # start chapter on any page, not just odd
    'extraclassoptions': 'openany',
    #
    # Value that prefixes 'release' element on title page.; keep blank
    'releasename': " ",
    #
    # Sonny, Lenny, Glenn, Conny, Rejne, Bjarne and Bjornstrup
    # 'fncychap': '\\usepackage[Rejne]{fncychap}',
    # 'fncychap': '\\usepackage{fncychap}',
    #
    # font packages for maths display incase needed
    'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',
    #
    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '12pt',
    #
    # standard figure options
    'figure_align': 'htbp',
    #
    'tableofcontents': ' ',
    #
    # custom \\hrule replacement to match css for html hr
    'transition': '\n\n\\vspace{24pt} {\\color{Gainsboro} \\rule{\\linewidth}{4pt} } \\bigskip\n\n '
    #
}

# preamble is custom latex code for general pages

latex_elements['preamble'] = r'''
    %%% preamble
    %%% add number to subsubsection 2=subsection, 3=subsubsection
    %%% below subsubsection is not good idea.
    \setcounter{secnumdepth}{3}
    %
    %%%% Table of content upto 2=subsection, 3=subsubsection
    \setcounter{tocdepth}{2}

    \usepackage{amsmath,amsfonts,amssymb,amsthm}
    \usepackage{graphicx}

    %%% reduce spaces for Table of contents, figures and tables
    %%% it is used "\addtocontents{toc}{\vskip -1.2cm}" etc. in the document
    \usepackage[notlot,nottoc,notlof]{}

    \usepackage{color}
    \usepackage[dvipsnames*,svgnames]{xcolor}
    \usepackage{transparent}
    \usepackage{eso-pic}
    \usepackage{lipsum}

    %% spacing between line; \onehalfspacing \doublespacing
    \usepackage{setspace}
    \singlespacing

    %%%%%%%%%%% datetime
    \usepackage{datetime}
    \newdateformat{MonthYearFormat}{%
        \monthname[\THEMONTH], \THEYEAR}

    % \RequirePackage{tocbibind} %%% comment this to remove page number for following
    % \addto\captionsenglish{\renewcommand{\contentsname}{Table of Contents}}
    % \addto\captionsenglish{\renewcommand{\chaptername}{Chapter}}

    %%% mycode chapter heading colour \fontsize{48}{50}
    \makeatletter
        \ChTitleVar{\centering \color{NavyBlue} \Huge\py@HeaderFamily}
        \ChNameVar{\centering \color{NavyBlue} \Huge\py@HeaderFamily}
        \ChNumVar{\centering \color{NavyBlue} \Large\py@HeaderFamily}
        \ChRuleWidth{2pt}
    \makeatother

    %%reduce spacing for itemize
    % \usepackage{enumitem}
    % \setlist{nosep}

    '''

# Custom title page not done otherwise

latex_elements['maketitle'] = r'''
    \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1

    \begin{titlepage}
        \centering

        \vspace*{40mm} %%% * is used to force space from top since first time is normally ignored
        \textbf{\color{NavyBlue} \Huge {PC-Microbit-Micropython}}

        \vspace{10mm}
        \begin{figure}[!h]
            \centering
            \includegraphics[scale=1.0]{logo_navyblue.png}
        \end{figure}

        \vspace{10mm}
        \LARGE \color{NavyBlue} {GMC}

        \vspace{10mm}
        \large \color{NavyBlue} Created : Jan 2021

        \vspace*{-1mm}
        \large \color{NavyBlue} Last updated : \MonthYearFormat\today

    \end{titlepage}

    \clearpage
    \pagenumbering{roman}
    \tableofcontents
    \clearpage
    \pagenumbering{arabic}

    '''

# latex_elements['sphinxsetup'] expt codes
# Latex colours named see: https://www.latextemplates.com/svgnames-colors
# sphinx latex see https://www.sphinx-doc.org/en/master/latex.html
# InnerLinkColor default {rgb}{0.208, 0.374, 0.486}. linkcolor and citecolor.
# OuterLinkColor default {rgb}{0.216, 0.439, 0.388}. filecolor, menucolor, and urlcolor.
# TitleColor default {rgb}{0.126, 0.263, 0.361}. titles(as configured via use of package "titlesec".)

# do not use r' string for latex_elements['sphinxsetup'].

latex_elements['sphinxsetup'] = '''
    hmargin={0.7in,0.7in}, vmargin={0.7in,0.7in}, \
    verbatimwithframe=true, \
    verbatimsep = 1pt, \
    verbatimborder = 1.0pt, \
    VerbatimColor = {named}{white}, \
    VerbatimBorderColor = {named}{LightGrey}, \
    noteBorderColor = {RGB}{106, 176, 222}, \
    hintBorderColor = {RGB}{26, 188, 156}, \
    importantBorderColor = {RGB}{26, 188, 156}, \
    tipBorderColor = {RGB}{26, 188, 156}, \
    \
    warningBorderColor = {RGB}{240, 179, 126}, \
    attentionBorderColor = {RGB}{240, 179, 126}, \
    cautionBorderColor = {RGB}{240, 179, 126}, \
    dangerBorderColor ={RGB}{242, 159, 151}, \
    errorBorderColor = {RGB}{242, 159, 151}, \
    warningBgColor = {RGB}{255, 237, 204}, \
    attentionBgColor = {RGB}{255, 237, 204}, \
    cautionBgColor = {RGB}{255, 237, 204}, \
    dangerBgColor = {RGB}{253, 243, 242}, \
    errorBgColor = {RGB}{253, 243, 242}, \
    \
    warningborder = 1pt, \
    attentionborder = 1pt, \
    cautionborder = 1pt, \
    dangerborder = 1pt, \
    errorborder = 1pt, \
    \
    TitleColor = {named}{NavyBlue}, \
    InnerLinkColor= {named}{NavyBlue}, \
    OuterLinkColor= {named}{NavyBlue}, \
    \
    HeaderFamily=\\rmfamily\\bfseries\

    '''


latex_logo = '_static/logo_navyblue.png'

# sectioning defaults to chapter when using manual
latex_toplevel_sectioning = 'chapter'

# for manual can use report
latex_documents = [
    (master_doc, 'PC-Microbit-Micropython.tex', 'PC-Microbit-Micropython',
     'GMC', 'manual'),
]
