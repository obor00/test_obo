#!/bin/bash

test()
{
	if [ $# != 1 ] || [ $1 == "-h" ] || [ $1 == "--help" ]
	then
		echo "syntax $i"
		exit
	fi 
}

echo $#
echo $1
echo $*
test $*
echo "process"


