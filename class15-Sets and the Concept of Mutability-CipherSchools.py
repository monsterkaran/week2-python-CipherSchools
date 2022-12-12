'''
Lists -> ordered and can be indexed using positions
Dicts -> unordered and can be indexed using keys
Sets -> unordered and cannot be indexed
'''
a={1:2}
print(type(a))
a={1,2,3,4}
print(type(a))
for i in a:
    print(i)
a={1,2,3,4}
b={3,4,5,6}
print(a-b)
c=a.union(b)
print(c)
print(a.intersection(b))
a.add(1)
a.remove(4)
print(a)
a=[[""]*3]*3
a[1][1]="X"
a[0][2]="O"
print(a)
print(id(a[0][1]))
print(id(a[1][1]))
print(id(a[2][1]))
a=61486
b=61486
print(id(a))
print(id(b))
print(a is b)
a="hello"
print(hash(a))
