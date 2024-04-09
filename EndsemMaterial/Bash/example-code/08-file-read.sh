#!/bin/bash  

########## Method-1 via command substitution#########

echo -e "\n##Method-1## \n"
res=`cat file.txt`  
echo "$res"  

 
########## Method-2 via command substitution #########   
echo -e "\n##Method-2## \n"
val=$(<file.txt)  
echo "$val"



########## Method-3 read from specified file,  #########
#read: This is a built-in command that reads a line from standard input 
#In this case, from the file specified by redirection at the end 
#line is the name of the variable where each line of input will be stored. 
#You can choose any valid variable name here.
echo -e "\n##Method-3## \n"
file='file.txt'  
  
i=1  
if [ -f "$file" ]; then
	while read line; do  
		#Reading each line  
  		echo "Line No. $i : $line"  
  		i=$((i+1))  
	done < $file   
else
    echo "File not found: $file"
fi

########## Method-4 similar to above, except filename is coming as input argument. 
#Notice also -r option. 
#The -r option in the read command in Bash is used to prevent backslashes in the input 
#from being interpreted as escape characters. #########   

echo -e "\n##Method-4## \n"
# Check if the file name is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

file="$1"  # Assign the first argument to the variable 'file'

# Check if file exists
if [ ! -f "$file" ]; then
    echo "File not found: $file"
    exit 1
fi

# Read line by line from the file
while read -r line; do
    echo "Line: $line"
done < "$file"

###Method-1## 
#
#hi
#how
#are you \?
#
#I 
#am
#fine.
#
###Method-2## 
#
#hi
#how
#are you \?
#
#I 
#am
#fine.
#
###Method-3## 
#
#Line No. 1 : hi
#Line No. 2 : how
#Line No. 3 : are you ?
#Line No. 4 : 
#Line No. 5 : I
#Line No. 6 : am
#Line No. 7 : fine.
#
###Method-4## 
#
#Line: hi
#Line: how
#Line: are you \?
#Line: 
#Line: I
#Line: am
#Line: fine.