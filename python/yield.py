
def ff():
    print('in ff')
def ff2():
    print('in ff2')
    return 'yop'


def yield_func():
    toto = 3
    print ('begin yield')
    yield (ff())
    ret = yield (ff2())
    print ('was ',ret)
    print ('was ', i)
    print ('end yield')
    print ('toto=', toto)

my= yield_func()

for i in my:
    print('start',my, i)



