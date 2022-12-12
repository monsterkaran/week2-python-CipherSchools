# Other that 3 Datatypes all the datatypes in python are immutable
a=[1,2,3,4]
print(a)
b=["shubham",1,1.5,print]
print(b)
a=[1,2,3,4]
a[0]=100
print(a)
print(len([1,2,3,4]))
print("shubham"+"lakra")
print([1,2,3]+[4,5,6])
print([1]*4)
a=[1,2,3,4,5]
for x in a:
    print(x)
print("a" in "shubham")
print(1 in [1,2,3,4,5])
a=[1,2,3,4,5]
print(a[-1])
a=[1,2,3]
a.insert(1,100)
print(a)
a=[1,2,3,4]
a.append(5)
print(a)
a.pop(2)
print(a)
a=["jatin","krrish","shorya","shubham","kaushik"]
a.remove("kaushik")
print(a)
a=[4,1,2,3,2,6,4]
print(sorted(a))
print(a)
a.sort()
print(a)
a=[1,2,3,4,5]
a.reverse()
print(a)
b=[1,2,3,4,5]
print(list(reversed(b)))
print(b)
a=[1,2,3,4]
for x in map(lambda x: x**2,a):
    print(x)

a = map(int, input().split())
print(a)
print(",".join(["jatin","samarth","molly"]))
print()