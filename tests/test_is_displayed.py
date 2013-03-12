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
from doublex import Spy, called

from matchers import is_displayed


class TestDisplayed(object):
    def test_is_displayed_asks_the_element_if_it_is_displayed(self):
        matcher = is_displayed()
        selenium_element = Spy()

        matcher.matches(selenium_element)

        assert_that(selenium_element.is_displayed, is_(called()))

    def test_is_displayed_returns_if_the_element_is_displayed(self):
        matcher = is_displayed()
        with Spy() as selenium_element:
            selenium_element.is_displayed().returns(u'foo')

        assert_that(matcher._matches(selenium_element), is_(u'foo'))
