#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------------------------------------------
# INFO:
#-----------------------------------------------------------------------------------------------------------------------

"""
Autor: Evan Hubinger, překlad Jaroslav Kubias
Licence: Apache 2.0
Description: Sphinx configuration file for the Coconut Programming Language.
"""

#-----------------------------------------------------------------------------------------------------------------------
# IMPORTS:
#-----------------------------------------------------------------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

import sys
import os.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from coconut.root import *  # NOQA

from coconut.constants import (
    version_str_tag,
    without_toc,
    with_toc,
)

from sphinx_bootstrap_theme import get_html_theme_path
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

#-----------------------------------------------------------------------------------------------------------------------
# DEFINITIONS:
#-----------------------------------------------------------------------------------------------------------------------

html_theme = "bootstrap"
html_theme_path = get_html_theme_path()

highlight_language = "coconut"

project = "Coconut"
copyright = "2015-2017, Evan Hubinger, licensed under Apache 2.0; Czech translation by Jaroslav Kubias"
author = "Evan Hubinger"
version = VERSION
release = version_str_tag

master_doc = "README"
source_suffix = [".rst", ".md"]
source_parsers = {
    ".md": CommonMarkParser
}
