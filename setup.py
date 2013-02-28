# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, u'README.md')).read()

requires = [
    u'pyHamcrest',
    u'lxml'
]

setup(
    version='0.17',
    name=u'matchers',
    description=u'Collection of highly reusable hamcrest matchers',
    long_description=README + u'\n',
    classifiers=[
        u"Programming Language :: Python",
        u"Topic :: Software Development :: Testing",
        u"Framework :: pyHamcrest",
        u"Operating System :: OS Independent",
    ],
    install_requires=requires,
    packages=find_packages(),
    test_suite=u'nose.collector',
    url=u'https://github.com/grupotaric/matchers',
    download_url=u'https://github.com/grupotaric/matchers/tags',
    author=uu'Taric S.A.',
    author_email=u'appregs@taric.es',
)
