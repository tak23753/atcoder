#!/bin/sh

# $1 contest_name

cd /workspace/code
acc new $1

dir_path="/workspace/code/$1/*"
dirs=`find $dir_path -maxdepth 0 -type d`
for dir in $dirs;
do
    cp ../snippet.py $dir/code.py
done
