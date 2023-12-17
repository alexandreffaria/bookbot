def countWords(text):
    wordsList = text.split()
    return len(wordsList)

def countLetters(text):
    countingDict = {}
    for letter in text:
        lowered = letter.lower()
        if lowered not in countingDict:
            countingDict[lowered] = 1
        else:
            countingDict[lowered] += 1
    return countingDict

frankenstein = "books/frankenstein.txt"
christmasCarol = "books/AChristmasCarolinProseBeingaGhostStoryofChristmas.txt"

with open(christmasCarol) as f:
    text = f.read()
    
    print(f"\n| Reporting on {christmasCarol} |\n")
    print(f"| {countWords(text)} words were found in the document.\n")

    letters = countLetters(text)
    list_letters = list(letters)
    list_letters.sort()
    
    for letter in list_letters:
        if letter.isalpha():
            print(f"| The '{letter}' character was found {letters[letter]} times.")

    print("\n| End of the report ~ Hope you are happy! ❤ |")