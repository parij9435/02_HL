# HL component 8 - set up score mechanics

# To do
# Set up round and win counter
# update feedback statements
import random

def intcheck(question, low=None, high=None):

   # sets up error messages
   if low is not None and high is not None:
            error = "please enter an integer between {} and {} " \
                    "(inclusive)".format(low,high)
   elif low is not None and high is None:
       error = "Please enter an integer that more than or " \
                "equal to {}".format(low)
   elif low is None and high is not None:
       error = "please enter an integer that is less or " \
                "equal to {}.".format(high)
   else:
       error = "Please enter an integer"

   while True:

        try:
            response = int(input(question))

            # checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue




rounds = intcheck("Rounds: ",1)
lowest = intcheck("Low Number: ")
highest = intcheck("High Number:", lowest + 1)
GUESSES_ALLOWED = 4

num_won=0
rounds_played = 0

while rounds_played < rounds:
    # Start of a round
    secret = random.randint(lowest, highest)

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

