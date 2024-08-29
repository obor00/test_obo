# exception propgatation

def a():
    print ('this is a bad computation')
    v = 5/0

def b():
    try:
        a()
    except Exception as e:
        print (f'b raise ecception {e}')
        raise e

def c():
    a()

def d():
    b()

def e():
    try:
        b()
    except:
        print (f'e raise ecception {e}, continue')

def aa():
    raise Exception('The value error exception')

def bb():
    aa()
    print('end of bb')

def cc():
    try:
        aa()
    except:
        print('cc got exception')

cc()
bb()

print ('calling e()')
e()
print ('calling d()')
d()
print ('calling c()')
c()
print ('calling b()')
b()
