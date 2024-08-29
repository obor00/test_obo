# class heritage

class Father:
    def __init__(self, val):
        self.val = val

    def pval(self):
        return (self.val)

class MyClass(Father):
    """A simple example class"""
    def __init__(self, val):
        super().__init__(val)
        self.val2 = self.val + 1


myc = MyClass( 123)
print ("myc.val:" + str(myc.val))
print ("myc.val2:" + str(myc.val2))
print (myc.pval())

myc = Father( 123)
print (myc.val)
print (myc.pval())

