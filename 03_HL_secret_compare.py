# HL component 3 - compares user guess with secret number

SECRET = 7

guess ""

while guess != SECRET:

    guess = int(input("Guess"))     # replace this with function call in dues course

    if guess < SECRET:
        print("Too High, try a lower number")
    elif guess > SECRET:
        print("Too Low, try a higher number")
    else:
        print("*****CONGRATULATIONS!    You Guessed the secret number*****")
