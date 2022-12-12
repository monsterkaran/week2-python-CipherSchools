# Dunders ( magic methods)(event methods)
# __<name of dunder>__
class Person:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print("Hello, my name is",self.name)
p=Person("Shubham")
p.say_hi()
print()
class A:
    def __init__(self):
        print(self)
        print("initialized")

    def __del__(self):
        print("I am dying")
a=A()
print(a)
del a
a=1
print(type(a))
print(a.__add__(5))
print("shubham".__mul__(2))
class A:
    a=1
    b=2

    def __add__(self, x):
        return self.a+self.b+x
a=A()
print(a+3)