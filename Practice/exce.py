num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

try:
    num3 = num1/num2
    print(f"The division of {num1} by {num2} is: {num3}")
except:
    print("The division of {num1} by {num2} is: {num3}")
