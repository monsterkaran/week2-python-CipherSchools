a = 5
print("value of a is %d" % a)
print("value of a is {}".format(a))
a, b, c = 1, 2, 3
print("a={2},b={1},c={0}".format(c, b, a))
n="Shubham"
c="LPU"
print("name = {name} company = {company}".format(name=n,company=c))
print(f"name = {n}")
# raw strings
print(len(r"a\nb"))
a="        shubham   k    "
print(a.strip())
print("1,2,3,4,5".split(","))
print("shubham".replace("h","t"))
print("shubham".count("h"))