# Minimal Sphinx configuration
import os
import sys

# Required Sphinx settings
project = 'pytracemalloc'
copyright = '2025, Author'
author = 'Author'

# Required Sphinx stubs
extensions = []
master_doc = 'index'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Basic theme setting (will be overwritten)
html_theme = 'alabaster'