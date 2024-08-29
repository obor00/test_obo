#!/bin/bash
# use: parser.sh < file.cfg

declare -A val
i=0
while read line ;  do
	 #echo $line
	keyword="${line/=*/}" 
	keyword="${keyword// /}"
	#echo  "keyword=${keyword}"

	value="${line/*=/}" ; 
	value=${value// /}
	val[$keyword]=$value
	#echo  ", value=${keyword}"
	i=$((i+1))
done 

#echo ${val[@]}

for key  in ${!val[@]} ; do
	echo "key=$key, value=${val[$key]}" 
done

# j=0
# while [ $j -lt $i ] ; do
# 	echo "key=${key[j]},val=${val[j]}"
# 	j=$((j+1))
# done
