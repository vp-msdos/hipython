name="Vishwas"
age=36
marks=99

employee = [name,age,marks] #lists are in order
print(employee)

#length of lists
print(len(employee))

#Slicing of list
print(employee[0:2:1])

#Repeatation of list
print(employee * 2)
twiceList = employee * 3
print(twiceList)

#append in lits
employee.append("Manager")
print(employee)

#Insert in list
employee.insert(0,"1")
print(employee)

"""
extend
remove
pop
"""
#append can only add one item at the end of list

employee.extend(["Accenture","Balaganj"])
print(employee)

#remove -- removes first occurence from the list
employee.remove(employee[-1])
print(employee)

#pop -- removes from the list based on index if we do not give any index it deletes last element

print(employee.pop(-1))
print(employee)