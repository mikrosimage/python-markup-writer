#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

dir_name = os.path.abspath(os.path.dirname(__file__))
toHtml_path = os.path.join(dir_name, 'pythonToHtml')
toLatex_path = os.path.join(dir_name, 'pythonToLatex')
toMarkdown_path = os.path.join(dir_name, 'pythonToMarkdown')

setup(
    name='MarkdownWriter',
    version='2.0',
    description='Markdown Writer API',
    keywords='Markdown',
    author='Valentin NOEL, Marc-Antoine ARNAUD',
    author_email='valent.noel@gmail.com',
    url='https://github.com/mikrosimage/python-markup-writer',
    packages=[
        'htmlwriter',
        'latexwriter',
        'markdownwriter',
        'pandocmarkdownwriter',
    ],
    package_dir={
        'htmlwriter': os.path.join(toHtml_path, 'htmlwriter'),
        'latexwriter': os.path.join(toLatex_path, 'latexwriter'),
        'markdownwriter': os.path.join(toMarkdown_path, 'markdownwriter'),
        'pandocmarkdownwriter': os.path.join(toMarkdown_path,
                                             'pandocmarkdownwriter'),
    },
    tests_require=['unittest2'],
    test_suite='tests',
)
