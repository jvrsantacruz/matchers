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

from matchers import has_properties


class Namespace(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


obj_properties = dict(a=1, b=2, c=3)
obj = Namespace(**obj_properties)
empty_obj = Namespace()


class TestHasProperties(object):
    def test_empty_object(self):
        assert_that(empty_obj, has_properties())

    def test_empty_object_dict_constructor(self):
        assert_that(empty_obj, has_properties({}))

    def test_kwargs_constructor(self):
        assert_that(obj, has_properties(**obj_properties))

    def test_dict_constructor(self):
        assert_that(obj, has_properties(obj_properties))
