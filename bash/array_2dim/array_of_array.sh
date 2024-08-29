#!/bin/bash 

declare -A JOB_LIST=(
   [aajob1]="a set of arguments"
   [bbjob2]="another different list"
   [ccjob3]="a third  different list"
)
sorted=($(printf '%s\n' "${!JOB_LIST[@]}"| /bin/sort))
for job in "${sorted[@]}"; do
   for args in "${job[@]}"; do
     echo "Do something with ${args} in ${job[$args]}"
   done
done
