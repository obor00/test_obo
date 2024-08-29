#!/bin/bash
set -eux


ffko()
{
    return 1
}

ffok()
{
    return 0
}

exit_error()
{
    if [ $? -ne 0 ] ; then
        echo "fail"
        exit
    else
        echo "OK"
    fi

}

ffok
exit_error

bash $0
echo "end of bash ffko"

ffko
exit_error


echo "end of test"


