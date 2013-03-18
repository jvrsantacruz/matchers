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

from matchers import assert_that_raises


class TestAssertThatRaises(object):

    def test_assert_that_raises_catches_the_specified_exception(self):
        with assert_that_raises(Warning):
            raise Warning()

    def test_assert_that_raises_AssertionError_on_unspecified_exception(self):
        try:
            with assert_that_raises(Warning):
                raise NameError()
        except AssertionError:
            pass

    def test_assert_that_raises_with_unspecified_exception_can_use_as_with_dict_with_exception(self):
        try:
            with assert_that_raises(Warning) as captured:
                raise NameError()
        except AssertionError:
            pass

        assert_that(captured, has_entry('exception', is_(instance_of(NameError))))

    def test_assert_that_raises_no_exception_can_use_as_with_dict_in_the_exception(self):
        try:
            with assert_that_raises(Warning) as captured:
                pass
        except AssertionError:
            pass

        assert_that(captured, has_entry('exception', is_(none())))

    def test_assert_that_raises_can_use_as_with_a_dict_containing_the_exception(self):
        with assert_that_raises(Warning) as captured:
            raise Warning()

        assert_that(captured, has_entry('exception', is_(instance_of(Warning))))

    def test_assert_that_raises_calls_matcher_on_exception(self):
        with assert_that_raises(instance_of(Warning)):
            raise Warning()

    def test_assert_that_raises_calls_matcher_on_exception(self):
        try:
            with assert_that_raises(instance_of(Warning)):
                raise NameError()
        except AssertionError:
            pass
