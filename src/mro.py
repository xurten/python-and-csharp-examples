"""
    Python resolves this using the C3 linearization algorithm to provide
    a deterministic MRO. It ensures that a class is always preceded by its
    subclasses in the MRO. This means that if a class inherits from multiple classes,
    Python will consider the methods from the left-most base class first,
    then the one to its right, and so on.
"""

class A(object):
    def dothis(self):
        print('I am from A class')


class B1(A):
    def dothis(self):
        print('I am from B1 class')
    # pass


class B2(object):
    def dothis(self):
        print('I am from B2 class')
    # pass


class B3(A):
    def dothis(self):
        print('I am from B3 class')


# Diamond inheritance
class D1(B1, B3):
    pass


class D2(B1, B2):
    pass


d1_instance = D1()
d1_instance.dothis()
print(D1.mro())


d2_instance = D2()
d2_instance.dothis()
print(D2.mro())