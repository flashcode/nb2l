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

"""nb2l tests."""

import mock
import pytest


def test_nb2l_invalid():
    """Test invalid numbers."""
    from nb2l import nb2l
    with pytest.raises(TypeError):
        nb2l()  # pylint: disable=no-value-for-parameter

    with pytest.raises(TypeError):
        nb2l('123')

    with pytest.raises(TypeError):
        nb2l(123.5)


def test_nb2l_simple():
    """Test simple numbers."""
    from nb2l import nb2l
    assert nb2l(0) == 'zéro'
    assert nb2l(1) == 'un'
    assert nb2l(5) == 'cinq'
    assert nb2l(10) == 'dix'
    assert nb2l(100) == 'cent'
    assert nb2l(123) == 'cent vingt-trois'
    assert nb2l(200) == 'deux cents'


def test_nb2l_large():
    """Test large numbers."""
    from nb2l import nb2l
    assert nb2l(123_456_789) == """\
cent vingt-trois millions \
quatre cent cinquante-six mille \
sept cent quatre-vingt-neuf\
"""
    assert nb2l(123_456_789_012) == """\
cent vingt-trois milliards \
quatre cent cinquante-six millions \
sept cent quatre-vingt-neuf mille \
douze\
"""
    assert nb2l(2_000) == 'deux mille'
    assert nb2l(2_000_000) == 'deux millions'
    assert nb2l(2_000_000_000) == 'deux milliards'
    assert nb2l(2_000_000_000_000) == 'deux billions'
    assert nb2l(2_000_000_000_000_000) == 'deux billiards'
    assert nb2l(2_000_000_000_000_000_000) == 'deux trillions'


def test_nb2l_overflow():
    """Test too big numbers."""
    from nb2l import nb2l
    with pytest.raises(OverflowError):
        assert nb2l(2_000_000_000_000_000_000_000)

    with pytest.raises(OverflowError):
        assert nb2l(2_000_000_000_000_000_000_000_000)

    with pytest.raises(OverflowError):
        assert nb2l(2_000_000_000_000_000_000_000_000_000)

    with pytest.raises(OverflowError):
        assert nb2l(2_000_000_000_000_000_000_000_000_000_000)


def test_nb2l_negative():
    """Test negative numbers."""
    from nb2l import nb2l
    assert nb2l(-0) == 'zéro'
    assert nb2l(-1) == 'moins un'
    assert nb2l(-123) == 'moins cent vingt-trois'


def test_main():
    import nb2l
    with pytest.raises(SystemExit):
        with mock.patch.object(nb2l.sys, 'argv', ['nb2l']):
            nb2l.main()
    with mock.patch.object(nb2l.sys, 'argv', ['nb2l', '123']):
        nb2l.main()
    with mock.patch.object(nb2l.sys, 'argv', ['nb2l', 'abc']):
        nb2l.main()


def test_init():
    import nb2l
    with mock.patch.object(nb2l, 'main', return_value=0):
        with mock.patch.object(nb2l, '__name__', '__main__'):
            with mock.patch.object(nb2l.sys, 'exit'):
                nb2l.init()
