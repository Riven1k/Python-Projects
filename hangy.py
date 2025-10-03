import random


# function display title used to display the "hangman" main title
def displayTitle(titleFilePath):
    # try used to allow for multiple exception errors
    try:
        fh = open(titleFilePath, "r")
    except FileNotFoundError:
        print("File Does not Exist, Closing Application")
    except IOError:
        print("Unable to open file due to I/O error, Closing Application")
    else:
        print(fh.read())
        fh.close


file = ("hangmanWord.txt")
displayTitle(file)


# function hangman drawings allows displays the hangman drawing .txt files
def loadHangmanDrawings(hangmanDrawingsFilePath):
    f = open(hangmanDrawingsFilePath, "r")
    hangmanLines = f.read().split("\n\n")  # \n\n used to separate the list when two blank lines are detected
    return hangmanLines
    f.close()


# function used to generate the random from the file
def generateRandomWord(wordsFilePath):
    # backup words incase file I/O error is presented
    backupWords = ["abruptly", "buffalo", "cricket", "duplex", "fashion", "galaxy"]

    try:
        word = (random.choice(open(wordsFilePath).read().split()).strip())  # random word chosen from the .txt file
        return word
    except FileNotFoundError:
        print("File Was not found, Closing Application")
    except IOError:
        print(random.choice(backupWords))


fileWords = ("ListOfWords.txt")
word = generateRandomWord(fileWords)

#output = [' _ '] * len(word)  # output underscores for all the letters in the random word chosen
incorrect_guesses = set()  # set for all incorrect guesses that are shown in curly brackets
drawingset = 0  # counter for printing the hangman drawings
hangmanLines = loadHangmanDrawings("hangmanDrawings3.txt")

# while loop used to display the drawings themselves
print(word)

while ''.join(output) is not word:
    print(hangmanLines[drawingset])
    print(''.join([x + " " for x in output]))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha():
        print("Only letters are allowed for guess:")

    # if statement used for printing the incorrect letters
    if guess not in word:
        incorrect_guesses.add(guess)
        print(incorrect_guesses)

        drawingset += 1

    # if statement for guessing the word
    if guess in word:
        print("Correct!", guess)
        for i, letter in enumerate(word):  # enumerate used to change underscores into the guessed letters
            if letter != '_' and guess == letter:
                output[i] = guess
                print(''.join(output))

    # simple elif statement used to print incorrect with each wrongly guessed letter
    elif guess not in word:
        print("Incorrect!", guess)

    # if statement used to congratulate user if user wins
    if ''.join(output) == word:
        print("Congrats you won the game!!")
        break

        # if word != ''.join(output):
        # print("You did not win, the word was: ",word)