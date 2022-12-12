# Comprehension
a=[]
for i in range(5):
    a.append(i)
print(a)
# list comprehension
a=[i**2 for i in range(5)]
print(a)
print()
a=list(map(lambda x: x**2,range(5)))
print(a)
a=[]
for i in range(5):
    temp=[]
    for j in range(5):
        temp.append(j)
    a.append(temp)
print(a)
'''
[ <value to apppend> <for statement> ... <if statement> ... ]
'''
a=[[j for j in range(5)] for i in range(5)]
print(a)
a=[[[(i,j)] for i in range(2)] for j in range(2)]
print(a)
n=5
a=[[max(i+1,j+1,n-i,n-j) for j in range(n)] for i in range(n)]
print(a)
# Dict comprehension
d={
    2:4,
    3:9,
    4:16
}
print(d)
d={i:i**2 for i in range(2,5)}
print(d)
# Set Comprehension
a={i for i in range(5)}
print(type(a))
a=(i for i in range(5))
print(type(a))
it=iter(a)
print(next(it))