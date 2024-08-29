
alist = [ 'a', 'b', 'c' ]

def test(p):
    print(p)
    return chr(ord(p)+ord('0'))

toto = {test(v):v for v in alist}
#print({test(v):v for v in alist})

print(toto)

titi = [test(v) for v in alist]
print(titi)
