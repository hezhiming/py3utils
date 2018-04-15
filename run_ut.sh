#!/usr/bin/env bash


_CUR_HOME=$(pwd)
_PYLINTRC='./pylintrc'

pylint --rcfile="$_PYLINTRC"  "./py3utils/"
python -m pytest --strict  --verbose  --cache-clear  tests/