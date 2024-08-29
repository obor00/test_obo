#!/bin/bash
lock_file=toto

get_lock()
{
	lockfile-create tutu
}

get_lock
echo "lock taken"


# to release
#lockfile-remove tutu
