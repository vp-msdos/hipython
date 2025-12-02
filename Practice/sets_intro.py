"""
Sets
Not Sequential collection
using {}
non repeated values
sets are mutable
"""

set1 = {1, 2, 3,"Vishwas",3}
print(set1)

t1 = list(set1)
print(t1)

t2 = tuple(set1)
print(t2)

print(len(set1))
print(type(set1))

#Operation in sets
#membership

print(1 in set1)
set1.add("Employee")
print(set1)

set1.remove(3)
print(set1)

#discard

set1.discard(3)
print(set1)

"""
Union(|), intersection(&), difference(-)
"""
set1 = {1, 2, 3,4}
set2 = {4, 5, 6}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))

#Frozen set immutable sets
fs1 = frozenset({1, 2, 3, 4})
print(fs1)
print(type(fs1))