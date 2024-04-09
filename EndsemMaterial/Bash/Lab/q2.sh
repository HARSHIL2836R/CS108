#!usr/bin/env bash

files=`find . -maxdepth 1 -type f -name "*.out"`
for file in $files
do
        echo $* >> $file
done