#!/bin/bash

set -e
set -x

test()
{
    [ "3" != "3" ] && exit 1
    return 0
}


test
exit 0
