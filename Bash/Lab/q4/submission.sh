#!/usr/bin/bash

# Set the LC_NUMERIC environment variable to use the C locale
export LC_NUMERIC=C

# Function to remove newline character
remove_newline() {
    echo "${1%"${1##*[![:space:]]}"}"
}

# Loop through each line in the input CSV file
while IFS=, read rollno quiz1 quiz2 midsem endsem marks; do
    echo "Processing $rollno"
    echo "Marks: $marks"
    
    # Remove newline character from marks
    marks=$(remove_newline "$marks")
    
    # Assign output files based on roll number prefix
    if [[ $rollno =~ ^"23" ]]; then
        echo "Writing to ug23.csv"
        output_file='ug23.csv'
    elif [[ $rollno =~ ^"24" ]]; then
        echo "Writing to ug24.csv"
        output_file='ug24.csv'
    else
        echo "Nothing"
    fi

    # Check if the current line is a header
    if [[ $rollno == "rollno" ]];then
		echo rollno,quiz1,quiz2,midsem,endsem,total-marks,grades > ug23.csv
		echo rollno,quiz1,quiz2,midsem,endsem,total-marks,grades > ug24.csv
    else
        # Assign grades based on marks and write to the output file
        if (( marks <= 35 )); then
            echo "${rollno},${quiz1},${quiz2},${midsem},${endsem},${marks},F" >> $output_file
        elif (( marks <= 45 )); then
            echo "${rollno},${quiz1},${quiz2},${midsem},${endsem},${marks},CC" >> $output_file
        elif (( marks <= 65 )); then
            echo "${rollno},${quiz1},${quiz2},${midsem},${endsem},${marks},BB" >> $output_file
        elif (( marks <= 85 )); then
            echo "${rollno},${quiz1},${quiz2},${midsem},${endsem},${marks},AB" >> $output_file
        else 
            echo "${rollno},${quiz1},${quiz2},${midsem},${endsem},${marks},AA" >> $output_file
        fi
    fi
done < "$1"
