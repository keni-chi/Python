class Calc: 
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def dif(self):
        return self.a - self.b


class Target(object):
    CONST_VALUE = 'foo'

    def get_const(self):
        return self.CONST_VALUE
