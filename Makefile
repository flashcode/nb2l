#
# Copyright (C) 2012-2023 Sébastien Helleu <flashcode@flashtux.org>
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

all: check

check: lint test

lint: flake8 pylint mypy bandit

flake8:
	flake8 . --count --select=E9,F63,F7,F82 --ignore=E203,W503 --show-source --statistics
	flake8 . --count --ignore=E203,W503 --exit-zero --max-complexity=10 --statistics

pylint:
	pylint nb2l

mypy:
	mypy --strict nb2l

bandit:
	bandit nb2l/nb2l.py

test:
	pytest -vv --cov-report term-missing --cov=nb2l
