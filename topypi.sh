#!/usr/bin/env bash
# Programm:
# History :
# Date    :2017/4/16
# Author  :hezhiming <he-zhiming{AT}foxmail.com>

PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

cd ./dist && rm -rf *

(python3 setup.py egg_info) && \
(python setup.py bdist_wheel --universal) && \
(twine register dist/*.whl) && \
(twine upload dist/*)
