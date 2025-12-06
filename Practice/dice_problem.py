"""
DIce
"""
import random
lt = [2,3,5,1,6]
while True:
    shuf = input("Shuffle the dice, write y for shuffle n for end :")
    if shuf == "y":
        random.shuffle(lt)
        print(f"Dice got : {random.choice(lt)}")
    else:
        print("Roll the dice stopped.")
        break

