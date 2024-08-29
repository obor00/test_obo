# class heritage

class A:
    class B:
        def __init__(self, val, father):
            self.val = val
            father.disp ('hello')

    def __init__(self, val):
        self.val1 = 'A'
        self.myB = self.B('B', self)

    def disp(self,v):
        print(v)

myc = A( 'A')
