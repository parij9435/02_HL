# HL - (and check) user input

# to do
# check a lowest is an integer (any integer)
# check that highest is more than lowest (lower bound only)
# check that round is more than 1 (upper ound only)
#  check that guess is between lowest and highest (lower and upper bound)


# number checking function goes here
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


# main routine

lowest = intcheck("Low Number: ")
highest = intcheck("High Number:", lowest + 1)
rounds = intcheck("Rounds: ",1)
guess = intcheck("Guess: ", lowest, highest)
