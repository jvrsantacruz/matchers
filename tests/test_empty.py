# -*- coding: utf-8 -*-

from hamcrest import *

from matchers import empty


class TestEmpty(object):
    def test_empty_dict(self):
        assert_that(dict(), is_(empty()))

    def test_empty_tuple(self):
        assert_that(tuple(), is_(empty()))

    def test_empty_list(self):
        assert_that(list(), is_(empty()))

    def test_empty_set(self):
        assert_that(set(), is_(empty()))

    def test_empty_unicode(self):
        assert_that(unicode(), is_(empty()))

    def test_empty_str(self):
        assert_that(str(), is_(empty()))


class TestNotEmpty(object):
    def setup(self):
        self.tuple = ((1, 2), (3, 4))

    def test_not_empty_dict(self):
        assert_that(dict(self.tuple), is_not(empty()))

    def test_not_empty_tuple(self):
        assert_that(self.tuple, is_not(empty()))

    def test_not_empty_list(self):
        assert_that(list(self.tuple), is_not(empty()))

    def test_not_empty_set(self):
        assert_that(set(self.tuple), is_not(empty()))

    def test_not_empty_unicode(self):
        assert_that(unicode('unicode'), is_not(empty()))

    def test_not_empty_str(self):
        assert_that(str('string'), is_not(empty()))
