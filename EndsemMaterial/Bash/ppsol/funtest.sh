#!usr/bin/env bash

run() {
    local n=$1
    for ((i=0;i<n;i++)); do
        echo Hi
    done
}

run $1