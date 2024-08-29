#!/bin/bash

declare -A parms=([aaa]="thisisa"  [bbb]="hereb")


declare -A job ; job[one]='!parms[@]'


echo ${!job[one]}
