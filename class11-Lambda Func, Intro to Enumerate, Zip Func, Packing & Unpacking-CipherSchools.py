show=print
show("something")
names=["jatin","saransh","shubham","samarth"]
for a in enumerate(names):
    print(a[0],a[1],a[0])
a=5
b=9
temp=a
a=b
b=temp
print(a,b)
print()
a=5
b=9
a=a^b
b=a^b
a=a^b
print(a,b)
a=5
b=9
a,b=b,a
print(a,b)
a=1,2
print(type(a))
for i,name in enumerate(names):
    print(i,"-",name)
print()
names=["jatin","saransh","shubham","samarth"]
scores=[50,80,90,70]
for name,score in zip(names,scores):
    print(name,"-",score)
