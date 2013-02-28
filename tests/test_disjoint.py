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

from matchers import disjoint_with


class TestDisjoint(object):
    def test_disjoint_with_is_positive_with_empty_sequences(self):
        assert_that([], is_(disjoint_with([])))

    def test_disjoint_with_is_positive_with_an_entirely_different_sequence(self):
        assert_that([1, 2, 3], is_(disjoint_with([4, 5, 6])))

    def test_disjoint_with_is_negative_with_a_partially_different_sequence(self):
        assert_that([1, 2, 3], is_not(disjoint_with([3, 4, 5])))

    def test_disjoint_with_is_negative_with_same_sequence(self):
        assert_that([1], is_not(disjoint_with([1])))

    def test_disjoint_with_accepts_generator_as_assert_data(self):
        assert_that((i for i in [1, 2, 3]), is_(disjoint_with([4, 5, 6])))

    def test_disjoint_with_accepts_generator_as_matcher_data(self):
        assert_that([1, 2, 3], is_(disjoint_with(i for i in [4, 5, 6])))
