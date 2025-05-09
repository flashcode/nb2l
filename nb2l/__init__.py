#!/usr/bin/env python3
#
# SPDX-FileCopyrightText: 2012-2025 Sébastien Helleu <flashcode@flashtux.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later
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

"""Convert numbers to literal French text."""

from .nb2l import (  # noqa: F401
    __version__,
    nb2l,
    main,
    init,
)

__all__ = (
    "__version__",
    "nb2l",
    "main",
    "init",
)
