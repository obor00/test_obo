
s1 = "toto"
s2 = "titi"
s3 = "toto"

res = (s1 == s2) or (s1 == s3)
res2 = (s1 == s3)

if res:
    print ("res ok")

if res2:
    print ("res2 ok")
