balance = 1500
def check_balance():
    return balance

def deposit(dipAmmount):
    global balance
    balance = dipAmmount + balance
    return balance

def withdraw(ammount):
    global balance
    balance = balance - ammount
    return balance



print("Welcome to banking application")

while True:
    print("Press 1 for balance check")
    print("Press 2 to deposit amount")
    print("Press 3 to withdraw amount")
    print("Press 4 to exit")
    user_input = input("Enter your choice: ")
    if user_input == "1":
        print(f"your balance is {check_balance()}")
    elif user_input == "2":
        depAm = float(input("Enter the amount you want to deposit: "))
        deposit(depAm)
        print(f"Your amount is deposited and your balance is {check_balance()}")
    elif user_input == "3":
        withAm = float(input("Enter the amount you want to withdrawal: "))
        withdraw(withAm)
        print(f"You have withdrawn {withAm} and your balance is {check_balance()}")
    elif user_input == "4":
        print("Thank you for using banking application")
        break