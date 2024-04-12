#!usr/bin/env bash

flag=0

for i in ${*:2}
do
if [ "$i" == "$1" ]; then
flag=1
echo YES
fi
done

if [ "$flag" == "0" ]; then
echo NO
fi