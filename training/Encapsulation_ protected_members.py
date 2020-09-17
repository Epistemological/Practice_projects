class Base:
    def __init__(self):
        self._a = 2
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ")
        print(self._a)

obj1 = Base()
print(obj1)
obj2 = Derived()