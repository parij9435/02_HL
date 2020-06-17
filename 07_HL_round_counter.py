# HL compont 7 - Generates desire number of rounds...

rounds = int(input("How many rounds? "))    # check with integer checker in due
rounds_played = 0

while rounds_played < rounds:
    print("Round {}".format(rounds_played+1))
    rounds_played += 1

    print("You have gotten to the end of the game")
