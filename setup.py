# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

requires = [
    'pyHamcrest',
    'lxml'
]

setup(
    name='matchers',
    description='Collection of highly reusable hamcrest matchers',
    version='0.17',
    long_description=README + '\n',
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
        "Framework :: pyHamcrest",
        "Operating System :: OS Independent",
    ],
    install_requires=requires,
    packages=find_packages(),
    test_suite='nose.collector',
    url='https://github.com/grupotaric/matchers',
    download_url='https://github.com/grupotaric/matchers/tags',
    author='Taric S.A.',
    author_email='appregs@taric.es',
)
