a=[1,2,3]
a[0]=100
a[2]=200
print(a)
a=(1,2,3,4)
print(type(a))
def func(*args):
    print(type(args))
func(1,2,3,4)
a=5
b=9
a,b=b,a
c=a,b
print(type(c))
def sum_diff(a,b):
    s=a+b
    d=a-b
    return s,d
c=sum_diff(10,5)
print(type(c))
print(c)
print()
a= 1,2,3,4
print(type(a))
print(list(range(5)))
print(tuple(range(5)))
a=(1,2,3,4)
a=[1,2,3,4]
a.append(5)
a.append(7)
a=dict()
a["name"]="shubham"
a[1]=100
a[(1,2)]=3
print(a)
a={
    "name":"shubham",
    1:100,
    (1,2):3
}
print(a)
a["name"]="Gaurav"
print(a)
# a[key]=values
key="marks"
if key in a:
    print(a[key])
else:
    print("key doesn't exist")
key="marks"
print(a.get(key))
key="name"
print(a.get(key,"key doesn't exist"))
print(a.keys())
print(a.values())
for key,value in a.items():
    print(key,"->",value)
print(a)
for x in a:
    print(x)
print(list(a))
# Challenge
n=int(input("how many records do you want to enter "))
l=[]
for i in range(n):
    l+=[{"roll-no":int(input("roll-no: ")),
         "name":input("name: "),
         "branch": input("branch: ")}]
print(l)
