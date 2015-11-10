import datetime
import sys
import os

try:
    __import__('imp').find_module('sphinx.ext.numfig')
    extensions = ['sphinx.ext.numfig']
except ImportError:
    # 'pip install sphinx_numfig'
    extensions = ['sphinx_numfig']

# numfig:
number_figures = True
figure_caption_prefix = "Fig."

source_suffix = '.rst'
master_doc = 'index'
pygments_style = 'sphinx'
html_use_index = False
html_theme = 'sphinx_rtd_theme'

pdf_documents = [('index', u'SFC', u'SFC Project', u'OPNFV')]
pdf_fit_mode = "shrink"
pdf_stylesheets = ['sphinx','kerning','a4']
#latex_domain_indices = False
#latex_use_modindex = False

latex_elements = {
    'printindex': '',
}

project = u'OPNFV: Service Function Chaining (SFC)'
copyright = u'%s, OPNFV' % datetime.date.today().year
version = u'1.0.0'
release = u'1.0.0'