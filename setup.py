#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Thanks to Kenneth Reitz, I stole the template for this

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

required = ['requests>=2.5', 'websocket-client==0.25.0', 'importlib>=1.0.3', 'beautifulsoup4==4.3.2']
packages = ['Slashchat', 'Slashchat.slackclient', 'Slashchat.plugins', 'Slashchat.plugins.meta']

#To add a message type, add appropriate entry to packages and for package_data
try:
    longdesc = open("README.rs").read()
except:
    longdesc = ''

setup(
    name='Slashchat',
    version='1.0.0',
    description='Simple and Clean Slack Chatbot',
    long_description=longdesc,
    author='Francesco Gramano',
    author_email='fran.gramano@mail.utoronto.ca',
    url='https://github.com/g2graman/Slashchat',
    packages=packages,
    scripts = ['bin/Slashchat'],
    package_data={'': ['limbo.LICENSE',], '': ['Slashchat/plugins/*.py', 'Slashchat/plugins/meta/*.py']},
    include_package_data=True,
    install_requires=required,
    license='MIT',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
