class bcolors:
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    ENDC = '\033[0m'


def  WordCheck(guess,word,GuessHistory, index):
    for n in range(0,5):
        if word[n] == guess[n]:
            GuessHistory[index] += str(f"{bcolors.GREEN}{guess[n]}{bcolors.ENDC}")
        elif word.find(guess[n]) != -1:
            GuessHistory[index] += str(f"{bcolors.YELLOW}{guess[n]}{bcolors.ENDC}")
        else:
            GuessHistory[index] += guess[n]


def WordFromUser(WordHistory):
    guess = input(":")
    
    while len(guess) != 5 or (guess in WordHistory) == True:
        print(f"{guess} already used or Not a 5 letter word")
        guess = input(":")

    WordHistory.append(guess)
    
    return guess


def DrawGameBoard(GuessHistory, AttemptCount, word):

    for n in range(0,AttemptCount):
        print(GuessHistory[n])

    for n in range(0, 6 - AttemptCount):
        print("▯▯▯▯▯")


def main():
    #List of words used (No Color/Formatting)
    WordHistory = []
    #List of words (Color+Formatting)
    GuessHistory = ["","","","","",""]

    print(f"{bcolors.GREEN}Welcome to Wordle enter a word{bcolors.ENDC}")

    word = "apple"

    for AttemptCount in range(1,7):
        guess = WordFromUser(WordHistory)
        print()
        WordCheck(guess,word,GuessHistory, AttemptCount-1)
        DrawGameBoard(GuessHistory, AttemptCount, word)


#This is so we can import the functions in this program in other code without having to run the main function
if __name__ == "__main__":
    main()