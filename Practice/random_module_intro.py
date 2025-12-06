"""
random function
"""
import random

for i in random.sample(range(10), 5):print(i)

print(random.randint(10,66))

#choice

li = [4,5,8,10,2]
print(random.choice(li))

#shuffle

lo = ["mango", "orange","apple"]
print(random.shuffle(lo))
print(lo)