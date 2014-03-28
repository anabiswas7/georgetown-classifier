#!/usr/bin/env python
# setup
# Setup script for gtml
#
# Author:   Benjamin Bengfort <bb830@georgetown.edu>
# Created:  Fri Mar 28 15:50:39 2014 -0400
#
# Copyright (C) 2014 Georgetown University
# For license information, see LICENSE.txt
#
# ID: setup.py [] bb830@georgetown.edu $

"""
Setup script for gtml
"""

##########################################################################
## Imports
##########################################################################

try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError:
    raise ImportError("Could not import \"setuptools\"."
                      "Please install the setuptools package.")

##########################################################################
## Package Information
##########################################################################

packages = find_packages(where=".", exclude=("tests", "bin", "docs", "fixtures",))
requires = []

with open('requirements.txt', 'r') as reqfile:
    for line in reqfile:
        requires.append(line.strip())

classifiers = (
    # TODO: Add classifiers
    # See: https://pypi.python.org/pypi?%3Aaction=list_classifiers
)

config = {
    "name": "GtML",
    "version": "0.1",
    "description": "A simple classifier",
    "author": "Benjamin Bengfort",
    "author_email": "bb830@georgetown.edu",
    "url": "https://github.com/bbengfort/georgetown-classifier",
    "packages": packages,
    "install_requires": requires,
    "classifiers": classifiers,
    "zip_safe": False,
    "scripts": ["bin/classify.py",],
}

##########################################################################
## Run setup script
##########################################################################

if __name__ == '__main__':
    setup(**config)
