#!/bin/bash

#the difference between " and '
myVariable="Hello, world\!"

echo myVariable
echo $myVariable
echo "$myVariable"
echo -e "$myVariable"
echo -E "$myVariable"
echo '$myVariable'
# The Output:
#myVariable
#Hello, world\!
#Hello, world\!
#Hello, world\!
#Hello, world\!
#$myVariable

#numbers are also strings
num1=1234
num2=7890
echo $num1$num2
#Output: 12347890

#Handling spaces
var="abc	xyz"
num="123"
echo 1 $var$num
echo 2 "$varXX$num"
echo 3 "${var}XX${num}"
echo 4 '$varXX$num'
#output 
#1 abc xyz123
#2 123
#3 abc   xyzXX123
#4 $varXX$num

echo word1	     word2
echo "word1	     word2"
#word1 word2
#word1        word2

#enviornment variables
echo $HOME # Home Directory  
echo $PWD # current working directory  
echo $BASH # Bash shell name  
echo $BASH_VERSION # Bash shell Version  
echo $LOGNAME # Name of the Login User  
echo $OSTYPE # Type of OS  

echo "User $LOGNAME is working in folder $PWD using OS $OSTYPE"

#command substitution in variables
lsResult=$(ls)
directory=`pwd`  
echo "My files are:" $lsResult  in $directory

#Use of double quotes. Double quotes (“”) preserve the literal 
#value of all characters with the exception of $, `, \
#what does above mean? In first two commands, 
#$ is interpreted as a variable with or  without quotes. 
#In the third command, bash intereprets * as wildcard and 
#lists all files ending in .sh. In the fourth, since it is 
#inside quotes, it views it as * character and looks for a file named "*.sh" 
echo $directory
echo "$directory"
ls *.sh
ls "*.sh"
ls \*.sh
#00-simple-script.sh  02-arithmetic.sh         04-command-line-arg.sh  06-local-global.sh  08-file-read.sh
#01-variables.sh      03-if-else-for-while.sh  05-function.sh          07-arrays.sh        var-demo-child.sh
#ls: cannot access '*.sh': No such file or directory
#ls: cannot access '*.sh': No such file or directory

