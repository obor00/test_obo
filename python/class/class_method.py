#
class Toto():

    gv = "first"
    v1 = 'abc'
    v2 = 'def' + gv

    @classmethod
    def setup(cls, v):
        print ('in setup')
        cls.v1 += v
        cls.gv = 'second'


Toto.setup('hello')

print(Toto.v1)
print(Toto.v2)
