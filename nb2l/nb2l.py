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

#
# Convert numbers to literal French text.
#
# Example:
#    $ python nb2l.py 123456
#    cent vingt-trois mille quatre cent cinquante-six
#
# History:
#
# 2017-02-19, Sébastien Helleu <flashcode@flashtux.org>:
#     version 1.0: first public release
# 2012-06-07, Sébastien Helleu <flashcode@flashtux.org>:
#     version 0.1: initial release
#

"""Convert numbers to literal French text."""

import sys

__version__ = '1.2-dev'

NB2L_NUMBER_1_99 = (
    'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf',
    'dix', 'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize',
    'dix-sept', 'dix-huit', 'dix-neuf', 'vingt', 'vingt et un',
    'vingt-deux', 'vingt-trois', 'vingt-quatre', 'vingt-cinq', 'vingt-six',
    'vingt-sept', 'vingt-huit', 'vingt-neuf', 'trente', 'trente et un',
    'trente-deux', 'trente-trois', 'trente-quatre', 'trente-cinq',
    'trente-six', 'trente-sept', 'trente-huit', 'trente-neuf', 'quarante',
    'quarante et un', 'quarante-deux', 'quarante-trois', 'quarante-quatre',
    'quarante-cinq', 'quarante-six', 'quarante-sept', 'quarante-huit',
    'quarante-neuf', 'cinquante', 'cinquante et un', 'cinquante-deux',
    'cinquante-trois', 'cinquante-quatre', 'cinquante-cinq',
    'cinquante-six', 'cinquante-sept', 'cinquante-huit', 'cinquante-neuf',
    'soixante', 'soixante et un', 'soixante-deux', 'soixante-trois',
    'soixante-quatre', 'soixante-cinq', 'soixante-six', 'soixante-sept',
    'soixante-huit', 'soixante-neuf', 'soixante-dix', 'soixante et onze',
    'soixante-douze', 'soixante-treize', 'soixante-quatorze',
    'soixante-quinze', 'soixante-seize', 'soixante-dix-sept',
    'soixante-dix-huit', 'soixante-dix-neuf', 'quatre-vingts',
    'quatre-vingt-un', 'quatre-vingt-deux', 'quatre-vingt-trois',
    'quatre-vingt-quatre', 'quatre-vingt-cinq', 'quatre-vingt-six',
    'quatre-vingt-sept', 'quatre-vingt-huit', 'quatre-vingt-neuf',
    'quatre-vingt-dix', 'quatre-vingt-onze', 'quatre-vingt-douze',
    'quatre-vingt-treize', 'quatre-vingt-quatorze', 'quatre-vingt-quinze',
    'quatre-vingt-seize', 'quatre-vingt-dix-sept', 'quatre-vingt-dix-huit',
    'quatre-vingt-dix-neuf',
)
NB2L_THOUSANDS = (
    'mille', 'million', 'milliard', 'billion', 'billiard', 'trillion',
)


def nb2l_version():
    """Return the nb2l version."""
    return __version__


def nb2l_add_hundreds(ngrp3):
    """Return string for hundreds."""
    res = ''
    if ngrp3 > 99:
        if ngrp3 // 100 > 1:
            res += NB2L_NUMBER_1_99[(ngrp3 // 100) - 1] + ' '
        res += 'cent'
        if ngrp3 // 100 > 1 and ngrp3 % 100 == 0:
            res += 's'
        if ngrp3 % 100 != 0:
            res += ' '
    if ngrp3 % 100 != 0:
        res += NB2L_NUMBER_1_99[(ngrp3 % 100) - 1]
    return res


def nb2l_add_thousands(ngrp3, nb3):
    """Return string for thousands."""
    res = ''
    if ngrp3 != 1 or nb3 != 1:
        res += ' '
    try:
        res += NB2L_THOUSANDS[nb3 - 1]
    except IndexError:
        raise OverflowError('Too many digits')
    if ngrp3 > 1 and nb3 > 1:
        res += 's'
    res += ' '
    return res


def nb2l(number: int) -> str:  # pylint: disable=too-many-branches
    """
    Convert an integer number (as string) to literal French text.

    :param: str,unicode: the number to convert, as string
            (from -999 999 999 999 999 999 999 to 999 999 999 999 999 999 999)
    :rtype: str
    :returns: literal French text
    """
    if not isinstance(number, int):
        raise TypeError('Number is not an integer')

    if number == 0:
        return 'zéro'

    res = ''

    if number < 0:
        # negative number
        res += 'moins '
        number *= -1

    str_number = str(number)

    nb3 = len(str_number) // 3
    nb3r = len(str_number) % 3
    if nb3r > 0:
        grp3 = str_number[0:nb3r]
        str_number = str_number[nb3r:]
    else:
        nb3 -= 1
        grp3 = str_number[0:3]
        str_number = str_number[3:]

    while nb3 >= 0:
        ngrp3 = int(grp3)
        if ngrp3 > 0:
            if ngrp3 != 1 or nb3 != 1:
                res += nb2l_add_hundreds(ngrp3)
            if nb3 > 0:
                res += nb2l_add_thousands(ngrp3, nb3)
        grp3 = str_number[0:3]
        str_number = str_number[3:]
        nb3 -= 1

    return res.rstrip()


def main():
    """Main function."""
    if len(sys.argv) < 2:
        sys.exit(f'Syntax: {sys.argv[0]} number [number...]')
    for number in sys.argv[1:]:
        try:
            print(nb2l(int(number)))
        except (ValueError, TypeError, OverflowError) as exc:
            print(f'{number}: {exc}')


def init():
    """Init function."""
    if __name__ == '__main__':
        main()


init()
