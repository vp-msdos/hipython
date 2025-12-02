"""
dictionary
Comma sperated key-value pair  within {}
"""
groceries = {'milk':60,'bread':20}
print(groceries)

print(groceries['milk'])
groceries['apple'] = 100
print(groceries)

#get
print(groceries.get('milk'))
print(groceries.get("banana"))
print(groceries.get("banana",40))

#membership
print("milk" in groceries)
print("egg" not in groceries)

#delete

groceries.pop("milk")
print(groceries)

#Allowed keys,, str, int,float, boolean, tuple all immutable
print(groceries.keys())
print(groceries.values())
print(groceries.items())


"""
Shallow and deep copy
list,set,dict
copy module does shallow copy
"""
import copy
l1 = [1,2,3,[4,10,6],"python"]
#shallow copy
l2 = copy.copy(l1)
print(l2)
l1[3][0]=100
print(l2)
print(l1)

l3 = copy.deepcopy(l1)
print(l3)
l1[1]=15
print(l1)
print(l3)





