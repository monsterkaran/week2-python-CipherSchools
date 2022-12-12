a = 5
b = 7
def show_loading():
    for i in range(3):
        print("loading","."*(i+1))
print(a+b)
show_loading()
print(a-b)
show_loading()
print(a*b)
show_loading()

def sheldon_knock(name):
    for _ in range(3):
        print("knock knock knock",name)
sheldon_knock("leonard")
def sheldon_knock(name, times = 3):
    for _ in range(times):
        print("knock knock knock",name)
print()
sheldon_knock("leonard")
print()
sheldon_knock("leonard", 5)
def add(a,b):
    return a + b
a=add(a,b)
print(a)