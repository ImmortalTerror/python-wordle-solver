# Modules
from requests import get  # Sends get requests to websites
from random import choice  # Picks random stuff from specified list
from termcolor import colored  # Makes colored text


# genWord Function
# Generates random word
allWords = get(
    "https://raw.githubusercontent.com/tabatkins/wordle-list/main/words"
).text.splitlines()


def genWord(length=0):
    """Generates random word of given length
    If no length was given, it will do any length
    Args: Length (int)
    Returns: string"""

    correctWords = []

    if length != 0:
        for word in allWords:
            if len(word) == length:
                correctWords.append(word)

        return choice(correctWords)
    else:
        return choice(allWords)


# Adds the colores to the guess. Basically the wordle in wordle
def match(guess, word):
    """Colours the letters in the guess that match the word
    Args: guess (string), word (string)
    Returns: string"""
    # checks if args are strings
    if type(guess) != str or type(word) != str:
        raise TypeError("Both arguments must be strings")

    # Checks if args are same length
    if len(guess) != len(word):
        raise ValueError("Strings must be the same length")

    solveList = [(), (), (), (), ()]
    # guess and word into lists of chars
    guessList = []
    wordList = []
    for i in guess:
        guessList.append(i)
    for i in word:
        wordList.append(i)

    # Finds exact matches
    for i in range(len(word)):
        if guessList[i] == wordList[i]:
            solveList[i] = (guessList[i], "green")
            guessList[i] = colored(guessList[i], "green")

    # Finds characters that are in the word but with the wrong index
    for i in range(len(word)):
        for c in range(len(guess)):
            if wordList[i] == guessList[c] and i != c:
                solveList[c] = (guessList[c], "yellow")
                guessList[c] = colored(guessList[c], "yellow")

    # Makes list for solver to read
    for i in range(len(guessList)):
        if len(guessList[i]) == 1:
            solveList[i] = [guessList[i], "grey"]

    # Turns list into str for output
    output = ""
    for i in guessList:
        output += i
    return [output, solveList]


def solver(guessOutput):
    goodWords = []
    greenChars = []

    # Get green characters and there index
    for char in range(len(guessOutput)):
        if guessOutput[char][1] == "green":
            greenChars.append([guessOutput[char][0], char])

    # Getting words with the green characters in the correct index
    count = 0
    for char in range(len(greenChars)):
        if count == 0:
            count += 1
            # Gets all possible words with the first green character in the correct index
            for word in allWords:
                if word[greenChars[char][1]] == greenChars[char][0]:
                    goodWords.append(word)
        else:
            # Filters for green characters in the correct indexes
            for word in goodWords:
                if word[greenChars[char][1]] != greenChars[char][0]:
                    goodWords.remove(word)

    return goodWords
