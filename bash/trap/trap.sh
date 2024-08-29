#!/bin/bash

export rootpid=$$

testname="toto"

ff()
{
   echo "ERROR EXIT: " >&2  && kill -s SIGUSR1 ${rootpid:-rootpid UNDEFINED}
   return 0
}

ff_exit()
{
    echo "This is exit function of test $testname"
}

err_set()
{
    echo "error trapped"
}


trap ff_exit  SIGUSR1 
trap err_set  ERR

set -e
false
#echo hello | grep fuu



ff



