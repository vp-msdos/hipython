"""
Number guessing game
User will start guessing the number
user will have 10 chances if guess we need to say congrats
otherwise end the game
"""
import random
print("Welcome to the game ! guess the number between 1 and 50")
num = random.randint(1,50)

x = 1
while x<=10:
    guess = int(input(f"Guess the number , try {x} :"))
    if(guess == num):
        print("You guessed right")
        break
    elif(guess > num):
        print("guessed number is greater!")
    else:
        print("guessed number is smaller!")
    x+=1
print("Thank you for playing")