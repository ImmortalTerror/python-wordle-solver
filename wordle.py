# Modules
from requests import get  # Sends get requests to websites
from random import choice  # Picks random stuff from specified list
from termcolor import colored  # Makes colored text


# genWord Function
# Generates random word
allWords = get(
    "https://raw.githubusercontent.com/tabatkins/wordle-list/main/words"
).text.splitlines()


def genWord(length: int = 0) -> list:
    """Generates random word of given length
    If no length was given, it will do any length
    Args: Length (int)
    Returns: list"""

    if length != 0:
        correctWords = [word for word in allWords if len(word) == length]

        return choice(correctWords)
    else:
        return choice(allWords)


# Adds the colores to the guess. Basically the wordle in wordle
def match(guess: str, word: str) -> list:
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
    guessList = [char for char in guess]
    wordList = [char for char in word]

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


def solver(guessOutput, goodWords=[]):

    # Sorts characters by colour, character and index into lists
    sortedChars = {
        "greenChars": [
            [guessOutput[char][0], char]
            for char in range(len(guessOutput))
            if guessOutput[char][1] == "green"
        ],
        "yellowChars": [
            [guessOutput[char][0], char]
            for char in range(len(guessOutput))
            if guessOutput[char][1] == "yellow"
        ],
        "greyChars": [
            [guessOutput[char][0], char]
            for char in range(len(guessOutput))
            if guessOutput[char][1] == "grey"
        ],
    }

    # Initial sort from allWords
    if sortedChars["greenChars"] != [] and goodWords == []:
        for char in range(len(sortedChars["greenChars"])):
            goodWords = [
                word
                for word in allWords
                if word[sortedChars["greenChars"][char][1]]
                == sortedChars["greenChars"][char][0]
            ]
    elif sortedChars["yellowChars"] != [] and goodWords == []:
        for char in range(len(sortedChars["yellowChars"])):
            goodWords = [
                word for word in allWords if sortedChars["yellowChars"][char][0] in word
            ]
    elif sortedChars["greyChars"] != [] and goodWords == []:
        for char in range(len(sortedChars["greyChars"])):
            goodWords = [
                word
                for word in allWords
                if sortedChars["greyChars"][char][0] not in word
            ]

    # Sorting from goodWords
    if sortedChars["greenChars"] != []:
        for char in range(len(sortedChars["greenChars"])):
            goodWords = [
                word
                for word in goodWords
                if word[sortedChars["greenChars"][char][1]]
                == sortedChars["greenChars"][char][0]
            ]

    if sortedChars["yellowChars"] != []:
        for char in range(len(sortedChars["yellowChars"])):
            goodWords = [
                word
                for word in goodWords
                if sortedChars["yellowChars"][char][0] in word
            ]

    if sortedChars["greyChars"] != []:
        for char in range(len(sortedChars["greyChars"])):
            goodWords = [
                word
                for word in goodWords
                if sortedChars["greyChars"][char][0] not in word
            ]

    nextGuess = choice(goodWords)
    goodWords.remove(nextGuess)
    return [nextGuess, goodWords]
