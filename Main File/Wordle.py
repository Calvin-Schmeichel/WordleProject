class bcolors:
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    ENDC = '\033[0m'


def WordCheck(WordLetterslist, guess, word, WordLetters, GuessHistory, index):
    
    for k in range(0, len(WordLetterslist)):

        ColorLimit = len(WordLetterslist[k])
        ColorCount = 0

        for n in range(0, len(WordLetterslist[k])):
            if word[WordLetterslist[k][n]] == guess[WordLetterslist[k][n]]:
                GuessHistory[index][WordLetterslist[k][n]] = str(f"{bcolors.GREEN}{GuessHistory[index][WordLetterslist[k][n]]}{bcolors.ENDC}")
                ColorCount += 1

        for n in range(0, 5):
            if (WordLetters[k] in guess) == True and (ColorLimit > ColorCount) and guess[n] == WordLetters[k] and (("32mp" in GuessHistory[index][n]) == False):
                GuessHistory[index][n] = str(f"{bcolors.YELLOW}{GuessHistory[index][n]}{bcolors.ENDC}")
                ColorCount += 1
    
    if guess == word:
        DrawGameBoard(GuessHistory, index+1)
        GameEndScreen(index+1, word)
        

def WordFromUser(WordHistory, GuessHistory):
    guess = input(":")
    
    while len(guess) != 5 or (guess in WordHistory) == True:
        print(f"{guess} already used or Not a 5 letter word")
        guess = input(":")

    WordHistory.append(guess)
    GuessHistory.append(list(guess))
    return guess


def DrawGameBoard(GuessHistory, AttemptCount):
    for k in range (0,AttemptCount):
        for n in range(0,5):
            print(GuessHistory[k][n], end = "")
        
        print()

    for n in range(0, 6 - AttemptCount):
        print("▯▯▯▯▯")


def GameEndScreen(AttemptCount, word):
    if AttemptCount < 7:
        print(f"{bcolors.GREEN}You guessed the word! in {AttemptCount} attempt(s)! {bcolors.ENDC}")
    else:
        print(f"{bcolors.YELLOW}You did not guess the word. The word was: {word}{bcolors.ENDC}")
        
        print()

    exit()

def main():
    #List of words used (No Color/Formatting)
    WordHistory = []
    #List of words (Color+Formatting)
    GuessHistory = []

    GameSquares = [["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"]]

    print(f"{bcolors.GREEN}Welcome to Wordle enter a word{bcolors.ENDC}")

    word = "bingo"

    WordLetters = (''.join(sorted(set(word))))
    WordLetterslist = []
   
    for n in range(0,len(WordLetters)):
        WordLetterslist.append([i for i, ltr in enumerate(word) if ltr == WordLetters[n]])
    
    for AttemptCount in range(1,7):
        guess = WordFromUser(WordHistory,GuessHistory)
        print()
        WordCheck(WordLetterslist, guess, word, WordLetters, GuessHistory, AttemptCount-1)
        DrawGameBoard(GuessHistory, AttemptCount)
    
    GameEndScreen(6, word)


#This is so we can import the functions in this program in other code without having to run the main function
if __name__ == "__main__":
    main()