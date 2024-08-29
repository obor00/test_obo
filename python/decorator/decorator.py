#import os

class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value - 10

    @x.deleter
    def x(self):
        del self._x

test = C()
test.x = 35
print(test.x)


