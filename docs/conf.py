# -- Sphinx configuration for OTCv8 docs ---------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'OTCv8 Dev — Dokumentacja'
author = ''
language = 'pl'

# Treat both .md and .rst as source
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Your docs already live in /docs with index.md at the root
root_doc = 'index'

extensions = [
    'myst_parser',
    'sphinx.ext.githubpages',   # drops .nojekyll for GitHub Pages
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
]

myst_enable_extensions = [
    'colon_fence', 'deflist', 'linkify', 'substitution',
    'replacements', 'smartquotes', 'attrs', 'tasklist',
]
myst_url_schemes = ('http', 'https', 'mailto')

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'furo'
html_static_path = ['_static']

# Optional: nicer anchor names
autosectionlabel_prefix_document = True

# Optional: Polish search and UI strings (Furo picks from language='pl')
# html_theme_options = {}
