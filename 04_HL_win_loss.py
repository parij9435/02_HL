# HL component 3 - comparesuser guess with secret number

# To Do
# set up number of guesses
# Count # of guesses
# if user runs out  of guesses, print 'you lose'
# if user guesses the secret number within the number of guesses print 'well done'

SECRET = 7
GUESS_ALLOWED = 4

# initialise variables
guesses_left = GUESS_ALLOWED
num_won = 0
guess = ""

# Start game
while guess != SECRET and guesses_left >=1:

    guess = int(input("Guess: "))   # replace this with function call in due cour
    guesses_left -= 1

    # If user has guesses left...
    if guesses_left >1:

        # if the guess is too high...
        if guess > SECRET:
            print("Too high.  Please try again")

        # if the guess is too low...
        elif guess < SECRET:
            print("Too low.  Please try again")

        # if the guess and secret number are the same
        else:
            print("You got it")


    # if the user is out of guesses
    else:
        # if the guess is too high...
        if guess > SECRET:
            print("Too high.  You lose")
        elif guess < SECRET:
            print("Too low.  You lose")
        else:
            print("You got it just in time")


