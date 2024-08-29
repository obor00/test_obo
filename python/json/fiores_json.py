#!/usr/bin/env python3

import re
import sys
import subprocess
import json
from typing import List, Dict
import yaml
import argparse

def decode_file(json_file):
    with open (json_file, "r")  as fp:
        file = json.load( fp)

    s = json.dumps( file, indent = 4 )

    #print(s)
    res = yaml.safe_load( s )
    #print( res)
    print( res['fio version'] )
    print( res['jobs'] [0] ['jobname'] )
    print( 'read IOPS     = ' + str(res['jobs'] [0] ['read'] ['iops']))
    print( 'write IOPS    = ' + str(res['jobs'] [0] ['write'] ['iops']))
    print( ' read bw      = ' + str(res['jobs'] [0] ['read'] ['bw']))
    print( 'write bw      = ' + str(res['jobs'] [0] ['write'] ['bw']))
    print( 'read latency  = ' + str(res['jobs'] [0] ['read'] ['lat_ns'] ['mean']))
    print( 'write latency = ' + str(res['jobs'] [0] ['write'] ['lat_ns'] ['mean']))


def main():
    parser = argparse.ArgumentParser()

    #parser.add_argument('command', type=str, choices=['discover', 'connect', 'disconnect'])
    parser.add_argument('-f', '--fio-json', type=str, help='fio result json file', required=True)

    # Arguments parsing
    args = parser.parse_args()

    # Arguments handling
    res = decode_file( args.fio_json )


if __name__ == '__main__':
    main()

