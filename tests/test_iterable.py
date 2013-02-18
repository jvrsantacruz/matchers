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

from matchers import iterable


class TestIterable(object):
    def test_list_is_iterable(self):
        assert_that(list(), is_(iterable()))

    def test_dict_is_iterable(self):
        assert_that(dict(), is_(iterable()))

    def test_tuple_is_iterable(self):
        assert_that(tuple(), is_(iterable()))

    def test_set_is_iterable(self):
        assert_that(set(), is_(iterable()))

    def test_generator_is_iterable(self):
        assert_that((i for i in []), is_(iterable()))

    def test_iterator_is_iterable(self):
        assert_that(iter([]), is_(iterable()))

    def test_string_is_iterable(self):
        assert_that(str(), is_(iterable()))

    def test_unicode_is_iterable(self):
        assert_that(unicode(), is_(iterable()))

    def test_custom_object_is_iterable(self):
        class IterateMe(object):
            l = list()
            def __iter__(self):
                return iter(l)

        assert_that(IterateMe(), is_(iterable()))

    def test_object_is_not_iterable(self):
        assert_that(object(), is_not(iterable()))

    def test_number_is_not_iterable(self):
        assert_that(0, is_not(iterable()))
