# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# Import datetime for date information:
import datetime

# -- Project information -----------------------------------------------------

current_year = datetime.datetime.now().year

project = 'COMET LiCSAR'
copyright = '{0}, COMET and CEMAC teams'.format(current_year)
author = 'COMET and CEMAC teams (Milan and Richard)'
email = 'cemac-support@leeds.ac.uk'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon'
#    'sphinx.ext.viewcode',
#    'sphinx.ext.autosummary'
]

# some fancy extensions for nicer overview...:

extensions += [
    'matplotlib.sphinxext.only_directives',
    'matplotlib.sphinxext.plot_directive',
    'matplotlib.sphinxext.ipython_directive',
    'matplotlib.sphinxext.ipython_console_highlighting']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add customised title sty file
latex_additional_files = ['_tex/customtitle.sty']

# Customise latex elements.
# Use openany + oneside to remove blank pages 
# Use customised title page
latex_elements = {
    'extraclassoptions': 'openany, oneside',
    'preamble': f'\\usepackage{{customtitle}}\n\\newcommand\\email{{{email}}}',
    'maketitle': '\\customtitle'
}

# Mock imports for autodoc building:
autodoc_mock_imports = [
    'astropy', 'cv2', 'matplotlib', 'numpy', 'osgeo', 'pandas', 'rioxarray',
    'scipy', 'sklearn', 'xarray'
]

# Order autodoc functions as they are in source:
autodoc_member_order = 'bysource'

# Don't show full paths in autodoc:
add_module_names = False

