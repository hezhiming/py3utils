#!/usr/bin/env bash

#set -ux
set -u

_CUR_DIR="$(pwd)"
_TESTS_HOME="./tests"
_PYTEST_CACHE="./.pytest_cache"
_PROJECT_NAME="py3utils"
_PROJECT_HOME="$_CUR_DIR/${_PROJECT_NAME}"
_JUNIT_XML="./junit_result.xml"


_COVERAGE_RC=".coveragerc"
_PYLINT_RC="./pylintrc"


function _run_pytest() {
#    py.test --verbose --cov="$_PROJECT_NAME" --cov-config "$_COVERAGE_RC"  --junit-xml="$_JUNIT_XML"  "$_TESTS_HOME"
    py.test --verbose --cov="$_PROJECT_NAME" --cov-config "$_COVERAGE_RC"  "$_TESTS_HOME"

    return "$?"
}

function _run_pylint() {
    pylint   --rcfile="$_PYLINT_RC"    "$_PROJECT_HOME"

    return "$?"
}

function _main() {
    # all should be success!
    # if not, $? will not be 0
    _run_pytest &&  _run_pylint

    if [[ "$?" == 0 ]]; then
        # all should be 0
        return 0
    else
        return 1
    fi
}

_main "${@}"






