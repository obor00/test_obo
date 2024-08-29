#!/bin/bash

[ $# -ne 1 ] && echo "Error missing parameter to $0" &&  exit                                                                        
host_id=$1  



declare -A v[$host_id]="hello"
declare -A u[$host_id]="obo"

#echo ${v[@]}

