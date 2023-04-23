#We import the "random" library so we can pick a random word for the answer
import random
#We import the "csv" library so we can read and import words from the .csv files
import csv
#We import the "os" library so we can clear the terminal screen to avoid clutter during gameplay
import os

#The "random_line" function gets a random word to use as the answer for the game
def random_line():

    #We open the .csv file
    inputFile = open("possiblewords.csv", "r")

    #We set the var "line" to the next function so we can grab the next word in the file
    line = next(inputFile)
    #We use a for loop to randomly grab a word from the file
    for num, aline in enumerate(inputFile, 2):
        #I got the syntax for this section from stackoverflow
        if random.randrange(num):
            continue
        line = aline
    #We close the file
    inputFile.close()
    #We return the chosen word to the main function
    return line

#The "ValidWord" function takes the word guessed by the player and makes sure it is a real
# five letter word in the english dictionary
def ValidWord(Guess):
    
    #We use the open loop from the "csv" library
    with open('validwords.csv', 'rt') as f:
        #we store the words in the reader var
        reader = csv.reader(f, delimiter=',')
        #We use nested for loops to manually check for a match
        #I got the syntax for this section from stackoverflow
        for row in reader:
            for field in row:
                if field == Guess:
                    return True     
    return False

#The "bcolors" class uses "ANSI escape sequences" for color formatting text in the terminal
class bcolors:
    #This mainly helps for readability of "GREEN" rather then "\u001b[32m"
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    GREY = '\u001b[2m'
    ENDC = '\033[0m'
    RED = '\033[91m'

"""
The "WordCheck" function is a monstrosity... we have to import so many vars and lists 
and readability is at a all time low. There is definitely better ways to make this function. 
Such as using a class but I did not have the time to do so. On that note I am proud of finding this
unique solution on my own without help from online resources. And it works for all of the edge cases!
"""
def WordCheck(WordLetterslist, guess, word, WordLetters, GuessHistory, index, GameSquares):
    
    #We have a for loop with two nested for loops 
    #This loops through by unique letter and decides if the letters in guess should be saved as green, yellow or white accordingly

    #"k" represents what list we are using inside the list of lists "WordLetterslist"
    #"k" =  list of letter indexes
    #"n" = index of letter
    for k in range(0, len(WordLetterslist)):
        #Inside the current list at index k is the list of indexs the current letter from the answer shows up in
        
        #Knowing that we can take the length of this list and store it into color limit
        #This prevents us from printing too many yellow letters in certain edge cases
        ColorLimit = len(WordLetterslist[k])
        #We will use ColorCount to keep track of green and yellow letters printed
        ColorCount = 0

        #This first for loop will iterate through the list of indexs using "n" for the green check
        for n in range(0, len(WordLetterslist[k])):
            #We then check if the letter in the answer at that index is the same letter at that index in the users guess
            #If they are we will change the letter to green in GuessHistory
            if word[WordLetterslist[k][n]] == guess[WordLetterslist[k][n]]:
                #We use the index var to make sure we are using the newest guess from "GuessHistory"
                #Here we are only changing the letters color not value
                GuessHistory[index][WordLetterslist[k][n]] = str(f"{bcolors.GREEN}{GuessHistory[index][WordLetterslist[k][n]]}{bcolors.ENDC}")
                #We match the color in "GameSquares" for the end of the game
                GameSquares[index][WordLetterslist[k][n]] = str(f"{bcolors.GREEN}▯{bcolors.ENDC}")
                #Since we changed a letter to green
                ColorCount += 1
            
        #This first for loop will iterate through the list of indexs using "n" for the yellow check
        for n in range(0, 5):
            """
            A few condtions must be met before a letter can be changed to yellow:
                1. The letter must be in the answer
                2. The letter must not already be green
                3. The color count for this letter must be below the limit (We can't print the letter yellow more then the amount of times it shows up in the answer)

                •"WordLetters[k] in guess) == True" is making sure the current letter is inside guess
                •"ColorLimit > ColorCount" is making sure we have not reached the color limit for the current letter
                •"guess[n] == WordLetters[k]" is making sure the current letter in guess is same as the current letter in WordLetters to prevent repeat logic
                •""32m" in GuessHistory[index][n]) == False" is making sure the current letter in the guess is not already green
            """
            if (WordLetters[k] in guess) == True and (ColorLimit > ColorCount) and guess[n] == WordLetters[k] and (("32m" in GuessHistory[index][n]) == False):
                GuessHistory[index][n] = str(f"{bcolors.YELLOW}{GuessHistory[index][n]}{bcolors.ENDC}")
                GameSquares[index][n] = str(f"{bcolors.YELLOW}▯{bcolors.ENDC}")
                ColorCount += 1

    #If the current player guess is the answer we can end the game early
    # we run the logic above first so the answer is show as all green on the gameboard since it is correct
    if guess == word:
        # Clearing the Screen
        os.system('cls')
        #We call the "DrawGameBoard" with the current attempt count
        DrawGameBoard(GuessHistory, index+1)
        #Once the final gameboard is drawn we call the "GameEndScreen" function to end the game with the current attempt count
        GameEndScreen(index+1, word, GameSquares)
        
#The "WordFromUser" function gets a input from the user and makes sure it is a valid input
def WordFromUser(WordHistory, GuessHistory, AttemptCount):
    #We store the input in guess
    guess = input(":")
    #We set the error var to "True" so we pass through all of the error checks at least once.
    #If we pass we will not loop. Otherwise we will loop till we get a valid input from the user.
    error = True
    #This will loop till we get a valid input from the user
    while error == True:
        #We remove all formatting from guess to avoid false error checks
        guess = (guess.lower()).replace(" ", "")

        #This makes sure the guess is five letters
        if len(guess) != 5:
            # Clearing the Screen
            os.system('cls')
            #We redraw the game
            DrawGameBoard(GuessHistory, AttemptCount-1)
            #We print the error message in red using the "bcolors" class
            print(f"{bcolors.RED}'{guess}' is not a 5 letter word{bcolors.ENDC}")
            guess = input(":")

        #This makes sure the guess has not been used yet
        elif (guess in WordHistory) == True:
            # Clearing the Screen
            os.system('cls')
            #We redraw the game
            DrawGameBoard(GuessHistory, AttemptCount-1)
            #We print the error message in red using the "bcolors" class
            print(f"{bcolors.RED}'{guess}' already used{bcolors.ENDC}")
            guess = input(":")

        #This makes sure the player has guessed a real word
        elif (ValidWord(guess)) == False:
            # Clearing the Screen
            os.system('cls')
            #We redraw the game
            DrawGameBoard(GuessHistory, AttemptCount-1)
            #We print the error message in red using the "bcolors" class
            print(f"{bcolors.RED}'{guess}' is not a real word{bcolors.ENDC}")
            guess = input(":")
        else:
            #if we pass all the error checks we can exit the loop
            error = False
        
    #We save the guess in "WordHistory" as a string
    WordHistory.append(guess)
    #We save the guess in "GuessHistory" as a list with each letter
    GuessHistory.append(list(guess))
    #we then return the guess value to the main function
    return guess

#The "DrawGameBoard" function draws the game board to the screen with all of 
# the up to date information including the players guess's and letters used in the QWERTY keyboard format
def DrawGameBoard(GuessHistory, AttemptCount):
    #We have two letter lists: 
    #"Alphabet" contains all letters in blank formatting for searching
    Alphabet = ["q", "w", "e", "r", "t","y", "u", "i", "o", "p","a", "s", "d", "f","g", "h", "j", "k", "l", "z", "x", "c", "v","b", "n", "m"]
    #"AlphabetFormatted" contains all letters with color formatting to print to the screen
    AlphabetFormatted = ["q", "w", "e", "r", "t","y", "u", "i", "o", "p","a", "s", "d", "f","g", "h", "j", "k", "l", "z", "x", "c", "v","b", "n", "m"]

    #We loop here for how many guesses the player has made so far
    #The first for loop "k" specifies the list index inside the list of lists
    for k in range (0,AttemptCount):
        print("      ", end = "")
        #The second loop "n" specifies the letter index inside the list inside the list
        for n in range(0,5):
            print(GuessHistory[k][n], end = "")
        #Once we have printed all the letters we make a return
        print()

    #For all of the remaining attempts we print blank ASCII squares
    for n in range(0, 6 - AttemptCount):
        print("      ▯▯▯▯▯")

    #This for loop is for printing the Alphabet in the QWERTY keyboard format.
    #We loop through every letter
    for letter in Alphabet:
        #We have three if statements that all check if the current letter with certain color formatting is contained in 
        # the list of lists "GuessHistory"
        #The snippet "(item for sublist in GuessHistory for item in sublist)" I got the syntax from stackoverflow

        #If the current letter is in the list of lists and is formatted green change the letters color to green in AlphabetFormatted
        if (f"{bcolors.GREEN}{letter}{bcolors.ENDC}" in (item for sublist in GuessHistory for item in sublist)) == True:
            AlphabetFormatted[Alphabet.index(letter)] = str(f"{bcolors.GREEN}{letter}{bcolors.ENDC}")
        #Else if the current letter is in the list of lists and is formatted yellow change the letters color to yellow in AlphabetFormatted
        elif (f"{bcolors.YELLOW}{letter}{bcolors.ENDC}" in (item for sublist in GuessHistory for item in sublist)) == True:
            AlphabetFormatted[Alphabet.index(letter)] = str(f"{bcolors.YELLOW}{letter}{bcolors.ENDC}")
        #Else if the current letter is in the list of lists then change the letters color to grey in AlphabetFormatted
        elif (letter in (item for sublist in GuessHistory for item in sublist)) == True:
            AlphabetFormatted[Alphabet.index(letter)] = str(f"{bcolors.GREY}{letter}{bcolors.ENDC}")
        #Else the letter will not be changed in AlphabetFormatted
    
    #We use a counter to keep track of what position we are in on the QWERTY keyboard format
    counter = 1
    #The for loop prints all of the letters to the screen
    for letter in AlphabetFormatted:
        print(letter, end=" ")
        counter+=1
        #Once counter gets to 11 or 20 we return since that means we just printed "p" or "l"
        # That way we match the QWERTY keyboard format
        if (counter == 11):
            print()
            print(" ", end="")
        elif (counter == 20):
            print()
            print("  ", end="")
    print()

#The "GameEndScreen" function is only called when the game is finnished
def GameEndScreen(AttemptCount, word, GameSquares):
    #If AttemptCount is set to -1 that means the player has failed
    if AttemptCount != -1:
        print(f"{bcolors.GREEN}You guessed the word! in {AttemptCount} attempt(s)! {bcolors.ENDC}")
    else:
        #We set AttemptCount to 6 so we can print the GameSquares correctly
        AttemptCount = 6
        print(f"{bcolors.YELLOW}You did not guess the word. The word was: {word}{bcolors.ENDC}")
        
        print()

    #To match the origional game we print the blank color formatted ASCII squares to the screen
    #The first for loop "k" specifies the list index inside the list of lists
    for k in range (0,AttemptCount):
        #The second loop "n" specifies the letter index inside the list inside the list
        for n in range(0,5):
            print(GameSquares[k][n], end = "")
        
        print()
    #We use the "exit" function to end the program
    exit()

#The "GetWord" function is used to remove any formatting from the answer string 
# and split the letters into the correct lists
def GetWord():
    #We first get a random word from the random line function
    word = random_line()
    #For testing purposes
    word = "right"

    #This removes any formatting from the answer string
    #I got the syntax for this section from stackoverflow
    word = "".join(i for i in word if ord(i)<126 and ord(i)>31)
    
    #"WordLetters" is a list of unique letters from the answer
    # EX: 'apple' becomes [a, p, l , e] since we have two "p"'s
    #I got the syntax for this section from stackoverflow
    WordLetters = (''.join(sorted(set(word))))
    #"WordLetterslist" will be a list of lists containing the list of indexs for each unique letter
    #This will become usefull for the "WordCheck" function
    WordLetterslist = []
    
    #This for loop enters in the correct indexs as mentioned above
    for n in range(0,len(WordLetters)):
        #I got the syntax for this section from stackoverflow
        WordLetterslist.append([i for i, ltr in enumerate(word) if ltr == WordLetters[n]])

    #We then retrun these vars to the main function
    return WordLetters, WordLetterslist, word

#This is the main function. It handles calling all the subfucntions, mannages the game rounds and 
# declears the initial vars
def main():
    #"possiblewords.csv" means the any word in that file can be a possible answer. (AKA: Normal words)
    #"validwords.csv" means any word in that file is a valid word to guess but might not be the answer (AKA: Medical terms, etc)

    #List of words used (No Color/Formatting)
    WordHistory = []
    #List of words (Color+Formatting)
    GuessHistory = []
    #List of endgame squares
    GameSquares = [["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"]]
    #Quick directions on how to play
    print("How To Play:")
    print("•Guess the Wordle in 6 tries.")
    print("•Each guess must be a valid 5-letter word.")
    print("•The color of the letters will change to show how close your guess was to the word.")
    print(f"{bcolors.GREEN}Welcome to Wordle enter a word{bcolors.ENDC}")

    #We call the "GetWord" function to get a new answer
    WordLetters, WordLetterslist, word = GetWord()
    
    #This for loop runs the game and keeps track of the current AttemptCount
    #We start at attempt one and go to attempt 6
    for AttemptCount in range(1,7):
        #We get a guess from the user and store it in the guess var
        guess = WordFromUser(WordHistory,GuessHistory, AttemptCount)
        print()
        #We call the "WordCheck" function to get guess color formatted
        WordCheck(WordLetterslist, guess, word, WordLetters, GuessHistory, AttemptCount-1, GameSquares)
        # Clearing the Screen
        os.system('cls')
        #After clearing the screen we draw the GameBoard again
        DrawGameBoard(GuessHistory, AttemptCount)

    #If the game does not end within the loop that means the player has faild to guess the answer 
    # and we call the "GameEndScreen" function manually
    GameEndScreen(-1, word, GameSquares)


#This is so we can import the functions in this program in other code without having to run the main function
if __name__ == "__main__":
    main()

#Terminal print out
"""
      rents
      filed
      whelm
      pound
      maple
      ample
q w e r t y u i o p 
 a s d f g h j k l 
  z x c v b n m 
You guessed the word! in 6 attempt(s)! 
▯▯▯▯▯
▯▯▯▯▯
▯▯▯▯▯
▯▯▯▯▯
▯▯▯▯▯
▯▯▯▯▯
"""
