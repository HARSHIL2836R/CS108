#!usr/bin/env bash

for file in *.jpg; do
    if [ -f "$file" ]; then
        echo ${file%%.j*}
    fi
done