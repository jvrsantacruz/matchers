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

from matchers import has_keys


class TestHasKeys(object):
    def test_empty_dict(self):
        assert_that({}, has_keys([]))

    def test_args_constructor(self):
        assert_that(dict(key=1, key2=2), has_keys('key', 'key2'))

    def test_same_key(self):
        assert_that(dict(key=1), has_keys(['key']))

    def test_same_keys(self):
        assert_that(dict(key=1, key2=2), has_keys(['key', 'key2']))

    def test_different_key(self):
        assert_that(dict(key=1), is_not(has_keys(['nokey'])))

    def test_one_of_many_keys(self):
        assert_that(dict(key=1, key2=2), has_keys(['key']))

    def test_none_of_many_different_keys(self):
        assert_that(dict(key=1, key2=2), is_not(has_keys([u'ná'])))

    def test_with_keys_defined_in_a_generator(self):
        assert_that(dict(key=1), has_keys(k for k in ['key']))

    def test_with_matched_object_being_a_pair_sequence(self):
        assert_that((('key', 1),), has_keys(['key']))

    def test_with_matched_object_being_a_pair_sequence_generator(self):
        assert_that(((k, v) for k, v in dict(key=1).items()), has_keys(['key']))

    def test_with_matched_object_being_a_dictionary_generator(self):
        assert_that({k: v for k, v in dict(key=1).items()}, has_keys(['key']))
