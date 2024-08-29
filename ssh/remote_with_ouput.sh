#!/bin/bash

remote_ssh()
{
	echo "hello"
	ssh 127.0.0.1 $*
}

remote_ssh  $*
