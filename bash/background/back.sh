#!/bin/bash

command="TOTO=abcde ;  ls -al"

funct()
{
	while read line
	do
		sleep 1
		echo "Read line: $line"
	done < <($command)
}

funct
