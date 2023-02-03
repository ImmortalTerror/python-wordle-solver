from random import choice
from os import system, name

# print(
#     """Wordle ai
# Press ENTER to play

# Also this kinda sucks at guessing cause im lazy"""
# )
# input()
print("\nRequesting word list...\n")
from wordle import genWord, match, solver

system("cls" if name == "nt" else "clear")

startWords = [
    "crane",
    "salet",
    "soare",
    "trace",
    "serai",
    "arose",
    "tales",
    "cones",
    "hates",
    "audio",
]

while True:
    secret = genWord()
    x = match(choice(startWords), secret)
    print(x[0])

    guess = solver(x[1])

    while guess[0] != secret:
        x = match(guess[0], secret)
        print(x[0])

        guess = solver(x[1], guess[1], guess[2])

    print(f"{match(guess[0], secret)[0]}")
    input("Press ENTER to play again\n")
