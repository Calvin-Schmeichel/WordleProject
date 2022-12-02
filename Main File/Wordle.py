import random
import csv
import os

def random_line():

    inputFile = open("possiblewords.csv", "r")

    line = next(inputFile)
    for num, aline in enumerate(inputFile, 2):
        if random.randrange(num):
            continue
        line = aline

    inputFile.close()
    return line

def ValidWord(Guess):
    
    with open('validwords.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            for field in row:
                if field == Guess:
                    return True     
    return False

class bcolors:
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    GREY = '\u001b[2m'
    ENDC = '\033[0m'
    RED = '\033[91m'


def WordCheck(WordLetterslist, guess, word, WordLetters, GuessHistory, index, GameSquares):
    
    for k in range(0, len(WordLetterslist)):

        ColorLimit = len(WordLetterslist[k])
        ColorCount = 0

        for n in range(0, len(WordLetterslist[k])):
            if word[WordLetterslist[k][n]] == guess[WordLetterslist[k][n]]:
                GuessHistory[index][WordLetterslist[k][n]] = str(f"{bcolors.GREEN}{GuessHistory[index][WordLetterslist[k][n]]}{bcolors.ENDC}")
                GameSquares[index][WordLetterslist[k][n]] = str(f"{bcolors.GREEN}▯{bcolors.ENDC}")
                ColorCount += 1

        for n in range(0, 5):
            if (WordLetters[k] in guess) == True and (ColorLimit > ColorCount) and guess[n] == WordLetters[k] and (("32mp" in GuessHistory[index][n]) == False):
                GuessHistory[index][n] = str(f"{bcolors.YELLOW}{GuessHistory[index][n]}{bcolors.ENDC}")
                GameSquares[index][n] = str(f"{bcolors.YELLOW}▯{bcolors.ENDC}")
                ColorCount += 1
    
    if guess == word:
        # Clearing the Screen
        os.system('cls')
        DrawGameBoard(GuessHistory, index+1)
        GameEndScreen(index+1, word, GameSquares)
        

def WordFromUser(WordHistory, GuessHistory, AttemptCount):
    guess = input(":")
    error = True
    while error == True:
        if len(guess) != 5:
            # Clearing the Screen
            os.system('cls')
            DrawGameBoard(GuessHistory, AttemptCount-1)
            print(f"{bcolors.RED}'{guess}' is not a 5 letter word{bcolors.ENDC}")
            guess = input(":")
        elif (guess in WordHistory) == True:
            # Clearing the Screen
            os.system('cls')
            DrawGameBoard(GuessHistory, AttemptCount-1)
            print(f"{bcolors.RED}'{guess}' already used{bcolors.ENDC}")
            guess = input(":")
        elif (ValidWord(guess)) == False:
            # Clearing the Screen
            os.system('cls')
            DrawGameBoard(GuessHistory, AttemptCount-1)
            print(f"{bcolors.RED}'{guess}' is not a real word{bcolors.ENDC}")
            guess = input(":")
        else:
            error = False
        

    WordHistory.append(guess)
    GuessHistory.append(list(guess))
    return guess


def DrawGameBoard(GuessHistory, AttemptCount):
    Alphabet = ["q", "w", "e", "r", "t","y", "u", "i", "o", "p","a", "s", "d", "f","g", "h", "j", "k", "l", "z", "x", "c", "v","b", "n", "m"]
    AlphabetFormatted = ["q", "w", "e", "r", "t","y", "u", "i", "o", "p","a", "s", "d", "f","g", "h", "j", "k", "l", "z", "x", "c", "v","b", "n", "m"]

    for k in range (0,AttemptCount):
        print("      ", end = "")
        for n in range(0,5):
            print(GuessHistory[k][n], end = "")
        
        print()

    for n in range(0, 6 - AttemptCount):
        print("      ▯▯▯▯▯")

    for letter in Alphabet:
        """print(letter)
        print(letter in (item for sublist in GuessHistory for item in sublist))"""
        if (f"{bcolors.GREEN}{letter}{bcolors.ENDC}" in (item for sublist in GuessHistory for item in sublist)) == True:
            #AlphabetFormatted[Alphabet.index(letter)] = (f"\x1b[32m{letter}\x1b[0m")
            AlphabetFormatted[Alphabet.index(letter)] = str(f"{bcolors.GREEN}{letter}{bcolors.ENDC}")
        elif (f"{bcolors.YELLOW}{letter}{bcolors.ENDC}" in (item for sublist in GuessHistory for item in sublist)) == True:
            #AlphabetFormatted[Alphabet.index(letter)] = (f"\x1b[33m{letter}\x1b[0m")
            AlphabetFormatted[Alphabet.index(letter)] = str(f"{bcolors.YELLOW}{letter}{bcolors.ENDC}")
        elif (letter in (item for sublist in GuessHistory for item in sublist)) == True:
            #AlphabetFormatted[Alphabet.index(letter)] = (f"\x1b[2m{letter}\x1b[0m")
            AlphabetFormatted[Alphabet.index(letter)] = str(f"{bcolors.GREY}{letter}{bcolors.ENDC}")
    
    counter = 1
    for letter in AlphabetFormatted:
        print(letter, end=" ")
        counter+=1
        if (counter == 11):
            print()
            print(" ", end="")
        elif (counter == 20):
            print()
            print("  ", end="")
    print()


def GameEndScreen(AttemptCount, word, GameSquares):
    if AttemptCount != -1:
        """# Clearing the Screen
        os.system('cls')"""
        print(f"{bcolors.GREEN}You guessed the word! in {AttemptCount} attempt(s)! {bcolors.ENDC}")
    else:
        AttemptCount = 6
        """# Clearing the Screen
        os.system('cls')"""
        print(f"{bcolors.YELLOW}You did not guess the word. The word was: {word}{bcolors.ENDC}")
        
        print()

    for k in range (0,AttemptCount):
        for n in range(0,5):
            print(GameSquares[k][n], end = "")
        
        print()

    exit()

def GetWord():
    word = random_line()
    word = "right"
    word = "".join(i for i in word if ord(i)<126 and ord(i)>31)
  
    WordLetters = (''.join(sorted(set(word))))
    WordLetterslist = []
   
    for n in range(0,len(WordLetters)):
        WordLetterslist.append([i for i, ltr in enumerate(word) if ltr == WordLetters[n]])

    return WordLetters, WordLetterslist, word


def main():
    #List of words used (No Color/Formatting)
    WordHistory = []
    #List of words (Color+Formatting)
    GuessHistory = []

    GameSquares = [["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"]]

    
        
    print()

    print(f"{bcolors.GREEN}Welcome to Wordle enter a word{bcolors.ENDC}")

    WordLetters, WordLetterslist, word = GetWord()
    
    for AttemptCount in range(1,7):
        guess = WordFromUser(WordHistory,GuessHistory, AttemptCount)
        print()
        WordCheck(WordLetterslist, guess, word, WordLetters, GuessHistory, AttemptCount-1, GameSquares)
        # Clearing the Screen
        os.system('cls')
        DrawGameBoard(GuessHistory, AttemptCount)
        #print(GuessHistory)

    GameEndScreen(-1, word, GameSquares)


#This is so we can import the functions in this program in other code without having to run the main function
if __name__ == "__main__":
    main()