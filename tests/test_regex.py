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

from matchers import matches_re, date_iso


DATE_ISO_FORMAT = '2012-10-10T00:00:00'
DATE_ISO_FORMAT_SPACE = '2012-10-10 00:00:00'
DATE_ISO_FORMAT_SHORT = '2012-10-10'
DATE_ISO_FORMAT_MILISECONDS = '2012-10-10T00:00:00.2042342'
DATE_ISO_FORMAT_WRONG_ORDER = '10-2012-10'
DATE_ISO_FORMAT_WRONG_ORDER_1 = '21-10-2012'
DATE_ISO_FORMAT_WRONG_MONTH = '2012-13-10T00:00:00'
DATE_ISO_FORMAT_WRONG_DAY = '2012-10-40T00:00:00'
DATE_ISO_FORMAT_WRONG_HOUR = '2012-10-10T25:00:00'
DATE_ISO_FORMAT_WRONG_MIN = '2012-10-10T00:70:00'
DATE_ISO_FORMAT_WRONG_SEC = '2012-10-10T00:00:70'


class TestMatchesRe(object):
    def test_matches_text(self):
        assert_that('test', matches_re('test'))

    def test_finds_text(self):
        assert_that('...test....', matches_re('test'))

    def test_matches_regex(self):
        assert_that('ACAB', matches_re('[AB][BC][AB][BC]'))

    def test_finds_regex(self):
        assert_that('....ACAB....', matches_re('[AB][BC][AB][BC]'))


class TestMatchesDateISO(object):
    def test_matches_iso_date(self):
        assert_that(DATE_ISO_FORMAT, is_(date_iso()))
        assert_that(DATE_ISO_FORMAT_SPACE, is_(date_iso()))

    def test_matches_iso_date_with_miliseconds(self):
        assert_that(DATE_ISO_FORMAT_MILISECONDS, is_(date_iso()))

    def test_matchers_iso_date_without_time(self):
        assert_that(DATE_ISO_FORMAT.split('T')[0], is_(date_iso()))

    def test_matchers_iso_date_with_slash_separator(self):
        assert_that(DATE_ISO_FORMAT.replace('-', '/'), is_(date_iso()))

    def test_matchers_iso_date_with_different_order(self):
        assert_that(DATE_ISO_FORMAT_WRONG_ORDER, is_not(date_iso()))
        assert_that(DATE_ISO_FORMAT_WRONG_ORDER_1, is_not(date_iso()))

    def test_matchers_iso_date_with_wrong_month(self):
        assert_that(DATE_ISO_FORMAT_WRONG_MONTH, is_not(date_iso()))

    def test_matchers_iso_date_with_wrong_day(self):
        assert_that(DATE_ISO_FORMAT_WRONG_DAY, is_not(date_iso()))

    def test_matchers_iso_date_with_wrong_hour(self):
        assert_that(DATE_ISO_FORMAT_WRONG_HOUR, is_not(date_iso()))

    def test_matchers_iso_date_with_wrong_min(self):
        assert_that(DATE_ISO_FORMAT_WRONG_MIN, is_not(date_iso()))

    def test_matchers_iso_date_with_wrong_sec(self):
        assert_that(DATE_ISO_FORMAT_WRONG_SEC, is_not(date_iso()))
