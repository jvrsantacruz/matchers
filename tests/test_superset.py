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

from matchers import superset_of


class TestSuperset(object):
    def test_superset_of_empty_sequence_is_superset(self):
        assert_that([], is_(superset_of([])))

    def test_superset_of_same_sequence_is_superset(self):
        assert_that([1], is_(superset_of([1])))

    def test_superset_of_agrees_on_a_subset_sequence(self):
        assert_that([1, 2, 3], is_(superset_of([1])))

    def test_superset_of_accepts_generator_as_assert_data(self):
        assert_that((i for i in [1, 2, 3]), is_(superset_of([1])))

    def test_superset_of_accepts_generator_as_matcher_data(self):
        assert_that([1, 2, 3], is_(superset_of(i for i in [1])))

    def test_superset_of_disagrees_on_a_superset_sequence(self):
        assert_that([1], is_not(superset_of([1, 2, 3])))
