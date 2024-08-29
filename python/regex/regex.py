#!/usr/bin/python3

import re as regex

r = regex.compile ('\[job_')

print (r.match ('[job_readwrite_70]'))
print (r.match ('#[job_readwrite_70]'))

r = regex.compile (r'\[job_')

print (r.match ('[job_readwrite_70]'))
print (r.match ('#[job_readwrite_70]'))
