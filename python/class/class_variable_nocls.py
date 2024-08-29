#
class toto():
    conf = 'class_variable'
    def __init__(self, v):
        print ('self.conf before assignment', self.conf)
        self.conf = v
        print ('self.conf after assignment', self.conf)

    @classmethod
    def clean(cls):
        print ('clean class method: ', toto.conf)

    def show(self):
        print ('from object, self.conf ', self.conf)
        print ('from object, toto.conf ', toto.conf)
        toto.conf = 'newval'

t1 = toto('p1')
t2 = toto('p2')

t1.show()
t2.show()

toto.clean()
print (toto.conf)
