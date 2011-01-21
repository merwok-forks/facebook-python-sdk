#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distribute_setup import use_setuptools
use_setuptools()

from setuptools import find_packages
from setuptools import setup, find_packages

SHORT_DESCRIPTION = "Facebook Graph API Python library"
LONG_DESCRIPTION = """This client library is designed to support the Facebook
Graph API and the official Facebook JavaScript SDK, which is the canonical way
to implement Facebook authentication."""

setup(
    name='facebook-python-sdk',
    version='0.1',
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Facebook',
    url='http://github.com/facebook/python-sdk',
    package_dir={'': 'src'},
    py_modules=[
        'facebook',
    ],
    scripts = [
        'distribute_setup.py',
    ],
)
