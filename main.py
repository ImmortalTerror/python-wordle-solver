import os

print("Requesting word list...")
from wordle import genWord, match, solver

os.system("cls" if os.name == "nt" else "clear")

# secret = genWord()
x = match("alrwt", "alert")
print(x[0])
print(x[1])

print(solver(x[1]))
