print("Requesting word list...\n")
from wordle import genWord, match, solver


for i in range(10):
    secret = genWord()

    x = match("slate", secret)
    print(x[0])

    guess = solver(x[1])

    while guess[0] != secret:
        x = match(guess[0], secret)
        print(x[0])

        guess = solver(x[1], guess[1])

    print(f"{match(guess[0], secret)[0]}\n")
