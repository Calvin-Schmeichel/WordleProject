class bcolors:
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    ENDC = '\033[0m'


def  WordCheck(guess,word,GuessHistory, index, WordHistory):
    GreenCount = -1
    for n in range(0,5):
        #print("guess find", word.find(guess[n]))
        #print("word find", word.find(word[n]))
        
        if word[n] == guess[n]:
            GuessHistory[index] += str(f"{bcolors.GREEN}{guess[n]}{bcolors.ENDC}")
            GreenCount += 1
        elif word.find(guess[n]) != -1 and word.find(guess[n]) >= word.find(word[n]):
            GuessHistory[index] += str(f"{bcolors.YELLOW}{guess[n]}{bcolors.ENDC}")
        else:
            GuessHistory[index] += guess[n]
    
    if guess == word:
        GameEndScreen(GuessHistory, index, word, guess, WordHistory)


def WordFromUser(WordHistory):
    guess = input(":")
    
    while len(guess) != 5 or (guess in WordHistory) == True:
        print(f"{guess} already used or Not a 5 letter word")
        guess = input(":")

    WordHistory.append(guess)
    
    return guess


def DrawGameBoard(GuessHistory, AttemptCount):

    for n in range(0,AttemptCount):
        print(GuessHistory[n])

    for n in range(0, 6 - AttemptCount):
        print("▯▯▯▯▯")

def GameEndScreen(GuessHistory, AttemptCount, word, guess, WordHistory):
    if AttemptCount != 6:
        print(f"{bcolors.GREEN}You guessed the word! in {AttemptCount+1} attempt(s)! {bcolors.ENDC}")
    else:
        print(f"{bcolors.YELLOW}You did not guess the word. The word was: {word}{bcolors.ENDC}")
    
    for k in WordHistory:
        guess = k
        for n in range(0,5):
            if word[n] == guess[n]:
                print(f"{bcolors.GREEN}▯{bcolors.ENDC}",end ="")
            elif word.find(guess[n]) != -1:
                print(f"{bcolors.YELLOW}▯{bcolors.ENDC}",end ="")
            else:
                print("▯",end ="")
        
        print()


    for n in range(0, 5 - AttemptCount):
        print("▯▯▯▯▯")

    exit()


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
        WordCheck(guess,word,GuessHistory, AttemptCount-1, WordHistory)
        DrawGameBoard(GuessHistory, AttemptCount)
    
    GameEndScreen(GuessHistory, AttemptCount, word, guess, WordHistory)


#This is so we can import the functions in this program in other code without having to run the main function
if __name__ == "__main__":
    main()