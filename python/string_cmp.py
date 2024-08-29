import sys
import re

vreg = re.compile ('toto.*')

s = "this is toto and follow"
s2 = "toto and next"

d =  vreg.match(s)
if d is not None:
    print ("d found")

d =  vreg.match(s2)
if d is not None:
    print ("s2 found")
print ("end of test")
