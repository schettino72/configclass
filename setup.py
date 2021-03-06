#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup

with codecs.open(
    os.path.join(os.path.dirname(__file__), 'README.rst'), 'r', 'utf8',
) as ld_file:
    long_description = ld_file.read()


setup (
    name = 'configclass',
    version = '0.2.0',
    author = 'Eduardo Naufel Schettino',
    author_email = 'schettino72@gmail.com',
    description = 'A Python to class to hold configuration values.',
    long_description = long_description,
    url = 'https://github.com/schettino72/configclass/',
    keywords = ['dict', 'config'],
    platforms = ['any'],
    license = 'MIT',
    py_modules = ['configclass'],
    install_requires = ['mergedict>=0.2.0'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
