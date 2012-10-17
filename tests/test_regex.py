# -*- coding: utf-8 -*-

from hamcrest import *

from matchers import matches_re


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
        pass
