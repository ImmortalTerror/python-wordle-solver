print("Requesting word list...\n")
from wordle import genWord, match, solver

secrete = genWord()
count = 1
x = match(genWord(), secrete)
print(x[0])
guess = solver(x[1])

while guess != secrete:
    count += 1
    x = match(guess, secrete)
    print(x[0])
    guess = solver(x[1])

count += 1
x = match(guess, secrete)
print(x[0])
print("bruh it worked")
print(f"took {count} guesses though")
