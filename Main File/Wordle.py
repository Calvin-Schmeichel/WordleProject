class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'

def  WordCheck(guess,word):
    for n in range(0,5):
        if word[n] == guess[n]:
            print(f"{bcolors.GREEN}{guess[n]}{bcolors.ENDC}",end ="")
        elif word.find(guess[n]) != -1:
            print(f"{bcolors.YELLOW}{guess[n]}{bcolors.ENDC}",end ="")
        else:
            print(guess[n],end ="")


def WordFromUser(GuessHistory):
    guess = input(":")
    

    while len(guess) != 5 or (guess in GuessHistory) == True:
        print(f"{guess} already used or Not a 5 letter word")
        guess = input(":")

        

    #rint(guess in GuessHistory)
    
    GuessHistory.append(guess)
    
    #print(guess)
    return guess

def DrawGameBoard(GuessHistory, AttemptCount, word):
    for n in GuessHistory:
        WordCheck(n, word)
        print()

    for n in range(0, 6 - AttemptCount):
        print("▯▯▯▯▯")


def main():
    GuessHistory = []

    print(f"{bcolors.GREEN}Welcome to Wordle enter a word{bcolors.ENDC}")

    word = "apple"

    #print(word[0])

    #print(word.find("a"))

    for AttemptCount in range(1,7):
        guess = WordFromUser(GuessHistory)
        print()
        #WordCheck(guess,word)
        DrawGameBoard(GuessHistory, AttemptCount, word)
        #print(GuessHistory)


#This is so we can import the functions in this program in other code without having to run the main function
if __name__ == "__main__":
    main()