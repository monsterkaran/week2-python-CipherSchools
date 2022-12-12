'''
Abstraction - need to know basis
Encapsulation
Polymorphism
Inheritance
'''
student={
    "name":"Shubham",
    "marks":50
}
student2={
    "name":"Samarth",
    "marks":48
}
'''
Python objects can have multiple traits
- callable (e.g. functions and classes)
- iterable (e.g. lists, string, generator)
- contextable (e.g. files)
'''
class Person:
    pass
p= Person()
print(p)
print(hex(id(p)))
a=1
class Person:
    name = "Shubham"
    def say_hi(self):
        print("Hello Everyone ! I am",self.name)
p = Person()
p.say_hi() # method call
Person.say_hi(p) # function call
