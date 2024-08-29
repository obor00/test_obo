t=["a1","a2"]
s= '.'.join(t)
type(t)
print t
print "%s" % t
fo=open("toto","w")
#fo.write("%s" %s)
fo.write("%s" % ','.join(t))
fo.close
fo=open("toto","r")
dd=fo.read()
print dd
print "%s" % dd
type(dd)
print len(set(t).intersection(dd))
if len(set(t).intersection(dd)) == 0:
    print "ok"
else:
	print "ko"

t2=["a3","a2"]
print len(set(t).intersection(t2))
if len(set(t2).intersection(dd)) == 0:
    print "ok"
else:
	print "ko"

if dd == s:
    print "OK"
else:
	print "KO"

s2=''.join(t2)
if dd == s2:
    print "OK"
else:
	print "KO"


if 'a1' in t:
    print ("key 'a1' is in")

print "end"
