<!--
SPDX-FileCopyrightText: 2017-2025 Sébastien Helleu <flashcode@flashtux.org>

SPDX-License-Identifier: GPL-3.0-or-later
-->

# Nb2l

[![PyPI](https://img.shields.io/pypi/v/nb2l.svg)](https://pypi.org/project/nb2l/)
[![Build status](https://github.com/flashcode/nb2l/workflows/CI/badge.svg)](https://github.com/flashcode/nb2l/actions?query=workflow%3A%22CI%22)
[![CodeQL](https://github.com/flashcode/nb2l/workflows/CodeQL/badge.svg)](https://github.com/flashcode/nb2l/actions?query=workflow%3A%22CodeQL%22)
[![REUSE status](https://api.reuse.software/badge/github.com/flashcode/nb2l)](https://api.reuse.software/info/github.com/flashcode/nb2l)

Nb2l is a Python script to convert numbers to literal French text.

Numbers from `-999 999 999 999 999 999 999` to `999 999 999 999 999 999 999` are accepted.

The script just requires Python ≥ 3.6.

## Examples

From Python:

```python
>>> from nb2l import nb2l
>>> nb2l(123456)
'cent vingt-trois mille quatre cent cinquante-six'
```

From command line:

```
$ nb2l 0 -15 123456 6824718
zéro
moins quinze
cent vingt-trois mille quatre cent cinquante-six
six millions huit cent vingt-quatre mille sept cent dix-huit
```

## Copyright

<!-- REUSE-IgnoreStart -->
Copyright © 2012-2025 [Sébastien Helleu](https://github.com/flashcode)

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
<!-- REUSE-IgnoreEnd -->
