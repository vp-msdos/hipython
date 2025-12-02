"""
Indentation with if block
"""

l = [1,2,3,"Vishwas"]
if l[0] == 2:
    print("correct")
print("Program finished")

#if else

year = int(input("Enter year: "))
if year > 2025:
    print("You are in future")
else:
    print("You are in past")

number = int(input("Enter number: "))
if number %2 == 0:
    print("Even")
else:
    print("Odd")

#if elif else
marks = float(input("Enter marks: "))
if marks >= 90:
    print("A")
elif marks >= 70 and marks < 90:
    print("B")
elif marks >= 60 and marks < 70:
    print("C")
else:
    print("fail")


#ternary

print("Even") if number % 2 == 0 else print("Odd")