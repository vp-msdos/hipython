"""
For loops
"""

l=[1,2,3,"Vishwas"]
for x in l: print(x)

#for loop for string
name = "vishwas"

for char in name: print(char.upper())
print(f"Length of name is {len(name)}")

#tuples

t1 = ("test,",1,2)
for t in t1: print(t)

#Dictionary

di = {"name": "vishwas", "age": 25}
for k, v in di.items(): print(k, v)
for k in di.keys(): print(k)

#With range
for x in range(10,1000,10): print(x)

for v in range(65,136): print(str(v))

#highest number in a list

li = [1,10,100,99,45,33,677]
max = li[0]
for x in li:
    if x > max:
        max = x
print(f"maximum number in lits is {max}")