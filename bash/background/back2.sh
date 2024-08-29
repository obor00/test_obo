#!/bin/bash

ff()
{
	echo "launching function ff, pid=$$"
    #sleep 30 < /dev/null > /dev/null &
    bash sleep.sh 
    res=$!
    echo $res
    return $res
}

ff1()
{
	echo "launching function ff1, pid=$$"
    ff
}


echo "my pid=$$"
ff1&
pid=$!

ps -ef | grep $pid
ps -ef | grep $$

echo "waiting pid $pid"
wait $pid
echo "end $pid "

