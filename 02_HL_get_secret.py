# HL component 2 - Generates random number between low and high.


import random

Low = 1
High = 4

for item in range(1, 20):
    secret = random.randint(Low, High)
    print(secret, end="\t")
    