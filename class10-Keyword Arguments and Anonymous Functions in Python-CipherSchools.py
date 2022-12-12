def hello():
    print("Hello World !")
a = 1
a = hello
print(a())
def func(a,b,c):
    print(a)
    print(b)
    print(c)
func(c=1,a=2,b=3)
def func(a):
    print(a)
func(1)
'''
Arguments in python

*Required arguments
*Default arguments
*Optional positional only arguments
*Required keyworded only arguments
*Default keyworded only arguments
*Optional keyworded only arguments
'''

def func(a,b):
    print(a,b)
func(1,2)
def func(a=1,b=2):
    print(a,b)
func()
func(1)
func(3,4)
def func(a,b,*c):
    print(a,b,c)
func(1,2,3,4)
def func(a,b,*c,d,e="jatin"):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
func(1,2,3,4,d="something",e="asdf")
def func(**k):
    print(k)
func(name="jatin")
# Anonymous functions or lambda functions
a=lambda a,b: a+b
print(a(1,2))
print(sorted([1,2,5,4,3]))