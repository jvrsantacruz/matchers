#!/bin/sh
FORMATS=gztar
python setup.py sdist --formats=${FORMATS}
PKG=`find dist -name "*.tar.gz" | sort -V | tail -n 1`
