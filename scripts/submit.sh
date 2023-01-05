#!/bin/sh

# $1 contest_name
# $2 problem_name

cd /workspace/code/$1/$2
acc submit code.py
