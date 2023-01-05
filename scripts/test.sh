#!/bin/sh

# $1 contest_name
# $2 problem_name

oj t -c "python3 /workspace/code/$1/$2/code.py" -d /workspace/code/$1/$2/tests/
