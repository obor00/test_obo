#!/bin/bash
lock_file=toto

get_lock()
{
	mkdir "${lock_file}" 2> /dev/null
	let v=$?
	while [ $v -ne 0 ]
	do
		echo "waiting"
		sleep 3
		mkdir "${lock_file}" 2> /dev/null
		let v=$?
	done
}

get_lock
echo "lock taken"

