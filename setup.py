# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='matchers',
    version='0.1',
    packages=find_packages(),
    install_requires=open('reqs.txt').read().splitlines(),
)
