#!usr/bin/env bash

if [ $# -ge 2 ]; then
        echo 'Usage: ./getEmails.sh <file>'
        exit 1
fi

if [ ! -f "$1" ]; then
        echo "Input File doesn't exists"
        exit 1
fi

#get emails from command substition
cat $1 | grep -E "[A-Za-z0-9]{1,}@[a-zA-Z]{1,}.iitb.ac.in" > emails.txt
sort -bdfr emails.txt > sortedEmails.txt
cat sortedEmails.txt | grep -E "[A-Za-z0-9]{1,}@cse.iitb.ac.in" > cseEmails.txt