#! /usr/bin/env python
# -*- coding: utf-8 -*-



"""Converter of value"""


from setuptools import setup, find_packages


classifiers = """\
License :: OSI Approved :: GNU Affero General Public License v3
Operating System :: POSIX
Programming Language :: Python
Topic :: Scientific/Engineering :: Information Analysis
"""

doc_lines = __doc__.split('\n')


setup(
    name = 'real_value',
    version = '0.1dev',
    author = 'Adrien Pacifico',
    author_email = 'adrienpacifico@gmail.com',
    classifiers = [classifier for classifier in classifiers.split('\n') if classifier],
    description = doc_lines[0],
    keywords = 'convert nominal to real value',
    license = 'http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    long_description = '\n'.join(doc_lines[2:]),
    url = 'https://github.com/adrienpacifico/real_value'
    )
