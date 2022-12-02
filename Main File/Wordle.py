class bcolors:
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    ENDC = '\033[0m'


def  WordCheck(guess,word,GuessHistory, index, GameSquares):

    for k in range(0,5):
        ColorCount = 0    
        for n in range(0,5):
            #print(word.count(guess[n]))
            if word[n] == guess[n]:
                GuessHistory[index][n] = str(f"{bcolors.GREEN}{GuessHistory[index][n]}{bcolors.ENDC}")
                GameSquares[index][n] = str(f"{bcolors.GREEN}▯{bcolors.ENDC}")
                ColorCount += 1
        for n in range(0,5):
            if (guess[n] in word) == True and ("32m" in GuessHistory[index][n]) == False and (word.count(word[k])) > ColorCount:
                GuessHistory[index][n] = str(f"{bcolors.YELLOW}{GuessHistory[index][n]}{bcolors.ENDC}")
                GameSquares[index][n] = str(f"{bcolors.YELLOW}▯{bcolors.ENDC}")
                ColorCount += 1

    if guess == word:
        GameEndScreen(index+1, word, GameSquares)
        

            
        
    

 




def WordFromUser(WordHistory, GuessHistory):
    guess = input(":")
    
    while len(guess) != 5 or (guess in WordHistory) == True:
        print(f"{guess} already used or Not a 5 letter word")
        guess = input(":")

    WordHistory.append(guess)
    GuessHistory.append(list(guess))
    #print(GuessHistory)
    return guess


def DrawGameBoard(GuessHistory, AttemptCount):
    for k in range (0,AttemptCount):
        for n in range(0,5):
            print(GuessHistory[k][n], end = "")
        
        print()

    for n in range(0, 6 - AttemptCount):
        print("▯▯▯▯▯")


def GameEndScreen(AttemptCount, word, GameSquares):
    if AttemptCount != 6:
        print(f"{bcolors.GREEN}You guessed the word! in {AttemptCount+1} attempt(s)! {bcolors.ENDC}")
    else:
        print(f"{bcolors.YELLOW}You did not guess the word. The word was: {word}{bcolors.ENDC}")
        
        print()

    

    for k in range (0,AttemptCount):
        for n in range(0,5):
            print(GameSquares[k][n], end = "")
            
        print()

    exit()

def main():
    #List of words used (No Color/Formatting)
    WordHistory = []
    #List of words (Color+Formatting)
    GuessHistory = []

    GameSquares = [["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"]]

    print(f"{bcolors.GREEN}Welcome to Wordle enter a word{bcolors.ENDC}")

    word = "apple"

    for AttemptCount in range(1,7):
        guess = WordFromUser(WordHistory,GuessHistory)
        print()
        WordCheck(guess,word,GuessHistory, AttemptCount-1, GameSquares)
        DrawGameBoard(GuessHistory, AttemptCount)
    
    GameEndScreen(AttemptCount, word, GameSquares)


#This is so we can import the functions in this program in other code without having to run the main function
if __name__ == "__main__":
    main()