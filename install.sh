#!/bin/sh
NAME=`python setup.py --name`
VER=`python setup.py --version`
VERNAME=$NAME-$VER

# Crea la versión
bash version.sh

# Descomprime e instala la versión
tar -xzf dist/$VERNAME.tar.gz
python $VERNAME/setup.py install
