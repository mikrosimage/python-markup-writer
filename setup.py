#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup

setup(
	name='MarkdownWriter',
	version='1.0',
	description='Markdown Writer API',
	author='Valentin NOEL, Marc-Antoine ARNAUD',
	author_email='valent.noel@gmail.com',
	url='https://github.com/mikrosimage/python-markup-writer',
	packages=['markdownwriter'],
    )

setup(
        name='PandocMarkdownWriter',
        version='1.0',
        description='Pandoc Markdown Writer API',
        author='Valentin NOEL, Marc-Antoine ARNAUD',
        author_email='valent.noel@gmail.com',
        url='https://github.com/mikrosimage/python-markup-writer',
        packages=['pandocmarkdownwriter'],
	install_requires = ['markdownwriter>=1.0'],
    )

