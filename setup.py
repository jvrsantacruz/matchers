# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

requires = [
    'pyHamcrest',
    'lxml'
]

setup(
    name='matchers',
    description='Custom Hamcrest matchers',
    version='0.17',
    long_description=README + '\n',
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
        "Framework :: pyHamcrest",
    ],
    install_requires=requires,
    packages=find_packages(),
    test_suite='nose.collector',
    url='http://www.taric.es',
    author='Taric S.A.',
    author_email='',
)
