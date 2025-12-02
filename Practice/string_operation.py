"""
Membership operations
in
"""
name="Vishwas is good"
print("is" in name)
print(str("GOOD") in name)

#not in

print("Singh" not in name)
print("good" not in name)

#Comparison of strings
print("Vishwas" == name[0:7])
print("VISHWAS".__eq__("Vishwas"))

#Removing spaces initial and trailing spaces using strip()
n = "The "
print(n.strip() == "The")

#Replace part of string using replace
print(name.replace("Vishwas","Arun"))

#Counting substring or string using count
print(name.count("Vishwas"))
print(name.count("i"))
print(f"Ocuurences of i in \"{name}\" is {name.count('i')}")

#Change cases of string
print(name.upper())
print(name.lower())
print(name.islower())
pq = "your name is ram"
print(name.title())

#Start and ending of string
print(name.startswith("Vishwas"))
print(name.endswith("d"))