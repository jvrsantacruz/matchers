#-*- coding: utf-8 -*-

from hamcrest import *
from matchers import has_len


class TestHasLenEmpty(object):
    def test_has_len_works_with_empty_lists(self):
        assert_that(list(), has_len(0))

    def test_has_len_works_with_empty_sets(self):
        assert_that(set(), has_len(0))

    def test_has_len_works_with_empty_tuples(self):
        assert_that(tuple(), has_len(0))

    def test_has_len_works_with_empty_dicts(self):
        assert_that(dict(), has_len(0))

    def test_has_len_works_with_any_empty_enumerable_object(self):
        class Collection(object):
            def __len__(self):
                return 0

        assert_that(Collection(), has_len(0))

    def test_has_len_works_with_empty_generators(self):
        assert_that((i for i in []), has_len(0))

    def test_has_len_works_with_empty_iterables(self):
        assert_that(iter([]), has_len(0))


class TestHasLenEmpty(object):
    def test_has_len_works_with_lists(self):
        assert_that([1, 2, 3], has_len(3))

    def test_has_len_works_with_sets(self):
        assert_that(set([1, 2, 3]), has_len(3))

    def test_has_len_works_with_tuples(self):
        assert_that((1, 2, 3), has_len(3))

    def test_has_len_works_with_dicts(self):
        assert_that({1: 1, 2: 2, 3: 3}, has_len(3))

    def test_has_len_works_with_any_enumerable_object(self):
        class Collection(object):
            def __len__(self):
                return 3

        assert_that(Collection(), has_len(3))

    def test_has_len_works_with_generators(self):
        assert_that((i for i in [1, 2, 3]), has_len(3))

    def test_has_len_works_with_iterables(self):
        assert_that(iter([1, 2, 3]), has_len(3))
