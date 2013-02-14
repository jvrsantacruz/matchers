# -*- coding: utf-8 -*-
"""
This file is part of matchers.

matchers is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

matchers is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with matchers.  If not, see <http://www.gnu.org/licenses/>.
"""

from hamcrest import *

from matchers import empty


class TestEmpty(object):
    def test_empty_dict(self):
        assert_that(dict(), is_(empty()))

    def test_empty_tuple(self):
        assert_that(tuple(), is_(empty()))

    def test_empty_list(self):
        assert_that(list(), is_(empty()))

    def test_empty_set(self):
        assert_that(set(), is_(empty()))

    def test_empty_unicode(self):
        assert_that(unicode(), is_(empty()))

    def test_empty_str(self):
        assert_that(str(), is_(empty()))

    def test_empty_generator(self):
        assert_that((a for a in list()), is_(empty()))

    def test_empty_iterator(self):
        assert_that(iter(list()), is_(empty()))


class TestNotEmpty(object):
    def setup(self):
        self.tuple = ((1, 2), (3, 4))

    def test_not_empty_dict(self):
        assert_that(dict(self.tuple), is_not(empty()))

    def test_not_empty_tuple(self):
        assert_that(self.tuple, is_not(empty()))

    def test_not_empty_list(self):
        assert_that(list(self.tuple), is_not(empty()))

    def test_not_empty_set(self):
        assert_that(set(self.tuple), is_not(empty()))

    def test_not_empty_unicode(self):
        assert_that(unicode('unicode'), is_not(empty()))

    def test_not_empty_str(self):
        assert_that(str('string'), is_not(empty()))

    def test_not_empty_generator(self):
        assert_that((i for i in range(1)), is_not(empty()))

    def test_not_empty_iterator(self):
        assert_that(iter([1]), is_not(empty()))
