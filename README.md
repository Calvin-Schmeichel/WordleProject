“Wordle” Documentation

This is a short document that will cover all of the functions and processes of the Wordle game for Python.

# Imports

These imports call on important libraries that we will use for the game.

We import the "random" library so we can pick a random word for the answer
We import the "csv" library so we can read and import words from the .csv files
We import the "os" library so we can clear the terminal screen to avoid clutter during gameplay

```python
    import random
    import csv
    import os
    import random_line
```

The "random_line" function gets a random word to use as the answer for the game. We first open the .csv file. Then set the variable "line" to the “next” function so we can grab the next word in the file. The for loop randomly grabs a word from the file. Finally we close the file and return the chosen word to the main function.

```python
    def random_line():


        inputFile = open("possiblewords.csv", "r")
        line = next(inputFile)


        for num, aline in enumerate(inputFile, 2):
            if random.randrange(num):
                continue


            line = aline


        inputFile.close()
        return line
```
# ValidWord

The "ValidWord" function takes the word guessed by the player and makes sure it is a real five letter word in the english dictionary. It first uses the open loop from the "csv" library (Mentioned above), then stores the words in the reader variable to then use a nested for loop to manually check for a match.

```python
    def ValidWord(Guess):
   
        with open('validwords.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                for field in row:
                    if field == Guess:
                        return True    
        return False
```

# bcolors

The "bcolors" class  uses "ANSI escape sequences" for color formatting text in the terminal. This mainly helps for readability. For example "GREEN" rather than "\u001b[32m".

```python
    class bcolors:
        #This mainly helps for readability of "GREEN" rather then "\u001b[32m"
        GREEN = '\u001b[32m'
        YELLOW = '\u001b[33m'
        GREY = '\u001b[2m'
        ENDC = '\033[0m'
        RED = '\033[91m'
```

# WordCheck

The "WordCheck" function is the main logic function for the game.  This function does have a few problems that could be refined in the future. Such as we have to import a ton of variables and lists and readability is a challenge with the current formatting. I believe there are better ways to make this function.
Such as using a class but I did not have the time to do so. On that note I am proud of finding this
unique solution on my own without help from online resources. And it works for all of the edge cases that I could think of!! And in its current form it should be modular for different length words such as 3 or 6 letter words in the future!

We have a for loop with two nested for loops. The first loop loops through by unique letter and decides if the letters in guess should be saved as green, yellow or white accordingly.

Loop variables to note:

"k" represents what list we are using inside the list of lists "WordLetterslist"
"k" =  list of letter indexes
"n" = index of letter

```python
    for k in range(0, len(WordLetterslist)):
```

Instead of looping by index 0-4 to compare the answer and the players guess (Which was the original approach). The function will loop by unique letters in the answer. This way we address all of the known edge cases. Such as too many yellow letters, yellow letters overriding green letters and more. We do this by keeping track of the number of times we print a yellow/green letter in ColorCount and always make sure it is less than or equal to ColorLimit which is the number of times that letter is used in the answer.

```python
    ColorLimit = len(WordLetterslist[k])
    ColorCount = 0
```

The function uses for loops for checking green and yellow letters. We first start with green. We have the list of indexes of the current letter and we use those to compare the letter values in the answer and in the player's guess. If they are the same we can print green (And add one to color count). If not we do nothing.

```python
    for n in range(0, len(WordLetterslist[k])):
    
        if word[WordLetterslist[k][n]] == guess[WordLetterslist[k][n]]:
        
            GuessHistory[index][WordLetterslist[k][n]] = str(f"{bcolors.GREEN}{GuessHistory[index][WordLetterslist[k][n]]}{bcolors.ENDC}")
        
            GameSquares[index][WordLetterslist[k][n]] = str(f"{bcolors.GREEN}▯{bcolors.ENDC}")
            ColorCount += 1
```

Then the function uses the second for loop to check for yellow letters. We use the same index logic as above for getting the unique letters in the answer but instead of checking if they are in the same position we are just checking if they are contained in the players guess or not. A few conditions must be met before a letter can be changed to yellow:

 The letter must be in the answer
 The letter must not already be green
 The color count for this letter must be below the limit (We can't print the letter yellow more then the amount of times it shows up in the answer)

If all of these conditions are met we can print the letter as yellow.

```python
    for n in range(0, 5):
    
    
    if (WordLetters[k] in guess) == True and (ColorLimit > ColorCount) and guess[n] == WordLetters[k] and (("32m" in GuessHistory[index][n]) == False):
                        
        GuessHistory[index][n] = str(f"{bcolors.YELLOW}{GuessHistory[index][n]}{bcolors.ENDC}")
                        
        GameSquares[index][n] = str(f"{bcolors.YELLOW}▯{bcolors.ENDC}")
                        
        ColorCount += 1
```

This function also has a check at the end that makes sure if the player guessed the word correctly it will end the game early.

```python
    if guess == word:
            os.system('cls')
            DrawGameBoard(GuessHistory, index+1)
            GameEndScreen(index+1, word, GameSquares)
```

# WordFromUser

The "WordFromUser" function gets an input from the user and makes sure it is a valid input. It first stores the user's input into the guess variable. Then starts the error detection while loop to make sure it is in fact a good input. 

```python
    def WordFromUser(WordHistory, GuessHistory, AttemptCount):
        guess = input(":")
        error = True
        while error == True:
```

We then strip the formatting from the users input:

```python
     guess = (guess.lower()).replace(" ", "")
```

If the users input is a five letter word:

```python
    if len(guess) != 5:
                os.system('cls')
                DrawGameBoard(GuessHistory, AttemptCount-1)
                print(f"{bcolors.RED}'{guess}' is not a 5 letter word{bcolors.ENDC}")
                guess = input(":")
```

A word the player has not guessed yet:

```python
    elif (guess in WordHistory) == True:
                os.system('cls')
                DrawGameBoard(GuessHistory, AttemptCount-1)
                print(f"{bcolors.RED}'{guess}' already used{bcolors.ENDC}")
                guess = input(":")
```

A real word in the english language:

```python
    elif (ValidWord(guess)) == False:
                os.system('cls')
                DrawGameBoard(GuessHistory, AttemptCount-1)
                print(f"{bcolors.RED}'{guess}' is not a real word{bcolors.ENDC}")
                guess = input(":")
```

Then we can return the guess to the main function knowing it is a good input. If not we loop till it is.

```python
    else:    
        error = False


    WordHistory.append(guess)
    GuessHistory.append(list(guess))

    return guess
```



# DrawGameBoard

The "DrawGameBoard" function draws the game board to the screen whenever called with all of the up to date information including the players guesses and letters used in the QWERTY keyboard format. 

It first will print all of the players guesses to the screen and then after print the remaining unused guess’s as blank ASCII squares.

```python
    for k in range (0,AttemptCount):
            print("      ", end = "")
            for n in range(0,5):
                print(GuessHistory[k][n], end = "")
            print()


    for n in range(0, 6 - AttemptCount):
            print("      ▯▯▯▯▯")
```

Once all of the guesses are printed. The function will then print the alphabet to the screen in the QWERTY keyboard format (Same order as your keyboard). It will loop through every letter in the alphabet and compare it to the color formatted guesses in the player's GuessHistory. If the letter shows up as green or yellow it will print accordingly (Green having priority over yellow. If it finds the letter as white then it will print the yellow as a dark gray to indicate the letter has been used. Otherwise the letter will be printed as the default format indicating it has not been used yet in a guess.

```python
    for letter in Alphabet:
    
    
    if (f"{bcolors.GREEN}{letter}{bcolors.ENDC}" in (item for sublist 
    in GuessHistory for item in sublist)) == True:
    
    
    AlphabetFormatted[Alphabet.index(letter)] = str(f"{bcolors.GREEN}{letter}{bcolors.ENDC}")
    
    
    elif (f"{bcolors.YELLOW}{letter}{bcolors.ENDC}" in (item for sublist in GuessHistory for item in sublist)) == True:
                
    AlphabetFormatted[Alphabet.index(letter)] = str(f"{bcolors.YELLOW}{letter}{bcolors.ENDC}")
    
    
    elif (letter in (item for sublist in GuessHistory for item in sublist)) == True:
    
    
    AlphabetFormatted[Alphabet.index(letter)] = str(f"{bcolors.GREY}{letter}{bcolors.ENDC}")
```

Once all of the letters are saved in the correct color formatt. The function will then print them to the screen, returning a new line twice (Using the counter variable) to match the three rows on the keyboard.

```python
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
```

# GameEndScreen

The "GameEndScreen" function is only called when the game is finished.

The function first uses a if statement to print a victory or defeat message to the screen.

```python
if AttemptCount != -1:
        print(f"{bcolors.GREEN}You guessed the word! in {AttemptCount} attempt(s)!       {bcolors.ENDC}")


    else:
        AttemptCount = 6
        print(f"{bcolors.YELLOW}You did not guess the word. The word was: {word}{bcolors.ENDC}")
       
        print()

Finally the function will then print the players guess history to the screen as ascii squares to mimic the original world game. And call the exit function to stop the program.

       for k in range (0,AttemptCount):
        for n in range(0,5):
            print(GameSquares[k][n], end = "")
       
        print()
        exit()
```

# GetWord

The "GetWord" function is used to remove any formatting from the answer string that was returned from the "random_line" function mentioned above. And then split the letters into the correct lists and store the indexes which will be used in the "WordCheck" function mentioned above.

```python
    def GetWord():
        word = random_line()
        word = "".join(i for i in word if ord(i)<126 and ord(i)>31)
        WordLetters = (''.join(sorted(set(word))))
        WordLetterslist = []
   
    for n in range(0,len(WordLetters)):
    WordLetterslist.append([i for i, ltr in enumerate(word) if ltr == WordLetters[n]])


    return WordLetters, WordLetterslist, word
```

# main

This is the main function. It handles calling all the subfunctions, manages the game rounds and declares the initial variables.

First the variables:

```python
    def main():


        WordHistory = []
        GuessHistory = []
        GameSquares = [["▯","▯","▯","▯","▯"],["▯","▯","▯","▯","▯"],
                       ["▯","▯","▯","▯","▯"],
                       ["▯","▯","▯","▯","▯"],
                       ["▯","▯","▯","▯","▯"],
                       ["▯","▯","▯","▯","▯"]]


        print("How To Play:")
        print("•Guess the Wordle in 6 tries.")
        print("•Each guess must be a valid 5-letter word.")
        print("•The color of the letters will change to show how close your guess was to the word.")
        print(f"{bcolors.GREEN}Welcome to Wordle enter a word{bcolors.ENDC}")


        WordLetters, WordLetterslist, word = GetWord()
```

The main function then uses a for loop to run the 6 rounds of the game. Inside the loop it calls the correct subfunctions to run the game. If we don’t exit early that means the player has failed and it calls the "GameEndScreen" function mentioned above.

```python
    for AttemptCount in range(1,7):
        guess = WordFromUser(WordHistory,GuessHistory, AttemptCount)
        print()
        WordCheck(WordLetterslist, guess, word, WordLetters, 
                  GuessHistory, AttemptCount-1, GameSquares)
        os.system('cls')
        DrawGameBoard(GuessHistory, AttemptCount)


    GameEndScreen(-1, word, GameSquares)

Finally we use an if statement to import the functions in this program in other code without having to run the main function (Such as for unit testing).

    if __name__ == "__main__":
        main()
```

# User Guide

The next few sections will contain a quick tutorial on how to play the game.

### Installation

Make sure to install all of the required files from Calvin Schmeichel’s OneDrive at this link:

https://mnscu-my.sharepoint.com/:f:/g/personal/tz5432sp_go_minnstate_edu/EoRpngwpKrFPtb8k8V88fYUBZ3kfCuDo-2ZHPMxWyYx6lQ?e=uSDjfv

Once the “Wordle”  folder is downloaded make sure Python 3.10 is installed on your computer more info at this link:

https://www.python.org/downloads/

### Startup

Once both of those downloads are done, open your command prompt (Windows) or terminal (Linux/macOS) and open the “Wordle”  folder.  Then type  the following command without the quotation marks:

“python3 ./wordV9.py”

### Gameplay
 
Once the program has started you should be greeted with a screen like this:
​​


After that you are all set! Start guessing 5 letter words! If you miss-type anything the program will reset your guess for you:



Keep playing until you guess the word!





