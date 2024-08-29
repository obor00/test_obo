# class heritage

def method1():
    class SimpleVar:
        def __init__(self):
            self.val = None
    return SimpleVar()

class toto:
    def __init__(self):
        self.myc = method1()

tutu = toto()
print("tutu.myc:",tutu.myc)
tutu.myc.val = 'hello'
print("tutu.myc:",tutu.myc)
print("tutu.myc.val:" + str(tutu.myc.val))
