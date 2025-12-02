"""
Tuple
Usage- months of year
data of tuple is immutable
Any data type could be used inside a tuple
tuple could be element of tuple
"""
t1 = (1, 2, 3, "Vishwas", [4,5,6])
print(t1)
print(len(t1))

print(t1[4])
print(type(t1))
t2 = list(t1)
print(t2)

#Operations on tuple
st1 = (1,2,3,"vishwas")
st2 = (4,5,6,"Employee")
st = st1 + st2
print(st)

#repeatation

print(st1*2)

#membership

print("vishwas" in st1)
print(99 not in st1)

print(id(st1))
