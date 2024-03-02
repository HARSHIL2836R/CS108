#!/bin/bash
while read -r line
do
        arr=($line)
        #arr[0]=rollno, arr[1]=name
        mv "${arr[0]}.pdf" "${arr[0]}_${arr[1]}.pdf" 2> /dev/null
done < $1