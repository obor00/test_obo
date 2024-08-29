#!/bin/bash 

set -u
set -x

log="namespace.log"
#log="namespace-$1.log"
exec &> >(tee $log)  2>&1



BLOCK_SIZE=4096
SEEK_BLOCK=16               # 65536 bytes
COUNT_BLOCK=3125000         # 12GB/4096
OUT_FILE_PREFIX=tmp_
let MAX_DISK=24
let MAX_NAMESPACE=32

usage()
{
        cat <<EOF
Usage: $0 <nb_ of_namespace>
or: $0 -h
<nb_of_namespace>: Number of namespace to test
-h| --help           this help
EOF
}


# check command line parameters
while getopts "h" option; do
        case "${option}" in
                h*)
                        usage
                        ;;
        esac
done

if [ $# -gt 1 ] ;
then
        usage
        exit 1
fi

nb_dd=${1-$MAX_NAMESPACE}  # max number of namespace to scany

 echo "fin"
