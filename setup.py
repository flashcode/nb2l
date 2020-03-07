#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2012-2020 Sébastien Helleu <flashcode@flashtux.org>
#
# This file is part of nb2l.
#
# Nb2l is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Nb2l is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with nb2l.  If not, see <https://www.gnu.org/licenses/>.
#

from setuptools import setup, find_packages
from nb2l import __version__ as nb2l_version

DESCRIPTION = 'Convert numbers to literal French text.'
LONG_DESCRIPTION = """
Nb2l converts numbers to literal French text.

Example::

    $ nb2l 0 -15 123456 6824718
    zéro
    moins quinze
    cent vingt-trois mille quatre cent cinquante-six
    six millions huit cent vingt-quatre mille sept cent dix-huit
"""

setup(
    name='nb2l',
    version=nb2l_version,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Sébastien Helleu',
    author_email='flashcode@flashtux.org',
    url='https://github.com/flashcode/nb2l',
    license='GPL3',
    keywords='number literal french',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 '
        'or later (GPLv3+)',
        'Natural Language :: French',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    packages=find_packages(),
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['nb2l=nb2l:main'],
    }
)
