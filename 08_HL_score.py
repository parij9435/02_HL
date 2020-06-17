# HL component 8 - set up score mechanics

# To do
# Set up round and win counter
# update feedback statements
import random

secret = 7
GUESSES_ALLOWED = 4
rounds = 3

num_won=0
rounds_played = 0

while rounds_played < rounds:
    # Start of a round

    # Output which round is being played
    print()
    print("Round {}".format(rounds_played + 1))

    guess = ""
    guesses_left = GUESSES_ALLOWED

    already_guessed =[]

    while guess != secret and guesses_left >=1:

        guess = int(input("Guess: "))
        rounds_played += 1

        if guess not in already_guessed:
            already_guessed.append(guess)
        else:
            print("You have already guessed that number.  Please try again.")
            continue

        guesses_left -=1

        if guesses_left >=1:

            if guess < secret:
                print("Too low, try a higher number.   Guesses left: {}".format(guesses_left))

            elif guess > secret:
                print("Too high, try a lower number.    Guesses left: {}".format(guesses_left))
        else:
            if guess < secret:
                print("Too low!")
            elif guess > secret:
                print("Too highh!")

    if guess == secret:
        if guesses_left == GUESSES_ALLOWED - 1:
            print("Amazing! You got it in one guess")
        else:
            print("Well done, you got it in {} guesses".format(len(already_guessed)))
            num_won += 1
    elif guesses_left < 1:
        print("Sorry - you lose this round as you have run out of guesses")

