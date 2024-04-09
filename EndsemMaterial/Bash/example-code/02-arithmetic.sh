#!/bin/bash

echo 1 5*2+1 
num=5*2+1
echo 2 $num

#Two formats, $((expression)) and $[expression]
echo 3 $((5*2+1)) 
echo 4 $[5*2+1] 
let num=5*2+1
echo 5 $num
declare -i result
result=5*2+1
echo 6 $result

#floating point needs use of bc
echo 7 $[3/4]
echo -n "8 "
echo "3/4" | bc -l

#OUTPUT
#1 5*2+1
#2 5*2+1
#3 11
#4 11
#5 11
#6 11
#7 0
#8 .75000000000000000000

#DESCRIPTION
#       bc  is a language that supports arbitrary precision numbers with interactive execution of statements.  There are some similarities in the syntax
#       to the C programming language.  A standard math library is available by command line option.  If requested, the math library is  defined  before
#       processing  any  files.   bc  starts by processing code from all the files listed on the command line in the order listed.  After all files have
#       been processed, bc reads from the standard input.  All code is executed as it is read.  (If a file contains a command to halt the processor,  bc
#       will never read from the standard input.)
#
#       This  version  of  bc  contains several extensions beyond traditional bc implementations and the POSIX draft standard.  Command line options can
#       cause these extensions to print a warning or to be rejected.  This document describes the language accepted by this processor.  Extensions  will
#       be identified as such.