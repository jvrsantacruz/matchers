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

from matchers import subset_of


class TestSubset(object):
    def test_subset_of_empty_sequence_is_subset(self):
        assert_that([], is_(subset_of([])))

    def test_subset_of_same_sequence_is_subset(self):
        assert_that([1], is_(subset_of([1])))

    def test_subset_of_agrees_on_a_superset_sequence(self):
        assert_that([1], is_(subset_of([1, 2, 3])))

    def test_subset_of_accepts_generator_as_assert_data(self):
        assert_that((i for i in [1]), is_(subset_of([1, 2, 3])))

    def test_subset_of_accepts_generator_as_matcher_data(self):
        assert_that([1], is_(subset_of(i for i in [1, 2, 3])))

    def test_subset_of_disagrees_on_a_subset_sequence(self):
        assert_that([1, 2, 3], is_not(subset_of([1])))
