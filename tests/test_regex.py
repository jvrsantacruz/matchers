# -*- coding: utf-8 -*-

from hamcrest import *

from matchers import matches_re, date_iso


DATE_ISO_FORMAT = '2012-10-10T00:00:00'
DATE_ISO_FORMAT_MILISECONDS = '2012-10-10T00:00:00.2042342'


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

    def test_matches_iso_date_with_miliseconds(self):
        assert_that(DATE_ISO_FORMAT_MILISECONDS, is_(date_iso()))

    def test_matchers_not_iso_date(self):
        assert_that(DATE_ISO_FORMAT.split('T')[0], is_not(date_iso()))
