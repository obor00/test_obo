#!/bin/bash

a_list=($(ls -l /))

sub()
{
	#local -n arr=$1
	for i in ${arr[@]}
	do
		echo $i"MMMMMM"
	done
}
echo ${a_list[@]}
echo "########################"
sub a_list
echo "########################"
sub ${a_list[@]}
echo "########################"

declare -A table
table[a1]="v1"
table[a2]="v2"
table[a-3]="v3"

echo ${table[@]}

indx="a1"
echo ${table[$indx]}
indx="a-3"
echo ${table[$indx]}
indx="a2"
echo ${table[$indx]}


source source.sh myname

indx="myname"

echo ${v[myname]}
echo ${u[$indx]}
