#HL component 6 - Statement Generator

def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print

# Main routine

too_low = hl_statement("^^ Too low, try a higher number.    |   "
                       "Guesses Left: 3 ^^", "^")
print()
too_high = hl_statement("vv too high, try a lower number.   |   "
                        "Guesses Left: 2vv" "v")
print()
duplicate = hl_statement("!! you already guessed that # Please try again.   |   "
                        "Gusses Left: 2 !!", "!" )
print()
well_done = hl_statement("*** Well done!    You got it in 3 guessese ***", "*")

print()
start_round = hl_statement("### Round 1 of 3 ###", "#")
