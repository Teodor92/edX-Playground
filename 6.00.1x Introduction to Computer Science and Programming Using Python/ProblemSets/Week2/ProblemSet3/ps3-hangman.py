def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if (not (letter in lettersGuessed)):
            return False;

    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    outputWord = ""

    for letter in secretWord:
        if (letter in lettersGuessed):
            outputWord += letter
        else:
            outputWord += "_"

    return outputWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    output = ""

    for letter in string.ascii_lowercase:
        if (not (letter in lettersGuessed)):
            output += letter
            
    return output  


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guessedLetters = []
    guessesLeft = 8

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is %s letters long." % str(len(secretWord)))
    print("-------------")

    while True:

        if (isWordGuessed(secretWord, guessedLetters)):
            print("Congratulations, you won!")
            break

        if (guessesLeft == 0):
            print("Sorry, you ran out of guesses. The word was %s." % secretWord)
            break

        print("You have %s guesses left." % str(guessesLeft))
        print("Available letters: %s" % getAvailableLetters(guessedLetters))

        letterGuess = input("Please guess a letter:")
        letterGuess = letterGuess.lower()
        
        if (letterGuess in guessedLetters):
            print("Oops! You've already guessed that letter: %s" % getGuessedWord(secretWord, guessedLetters))
            print("-------------")
            continue

        if (guessedLetters.count(letterGuess) == 0):
            guessedLetters.append(letterGuess)

        if (letterGuess in secretWord):
            print("Good guess: %s" % getGuessedWord(secretWord, guessedLetters))
        else:
            guessesLeft -= 1
            print("Oops! That letter is not in my word: %s" %getGuessedWord(secretWord, guessedLetters))

        print("-------------")