#!/bin/sh

USER=pypiserver
SERVER=s002htz
DIR=/home/pypiserver/packages
FORMATS=gztar

# Genera una nueva versión y la manda al pypiserver
python setup.py sdist --formats=${FORMATS}
PKG=`find dist -name "*.tar.gz" | sort -V | tail -n 1`
scp ${PKG} ${USER}@${SERVER}:${DIR}
