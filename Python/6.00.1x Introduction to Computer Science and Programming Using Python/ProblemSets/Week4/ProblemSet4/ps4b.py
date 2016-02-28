from ps4a import *
import time


#
# Test word validity
#
def isCompValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    for letter in word:
        letterCount = hand.get(letter, 0)

        if letterCount == 0:
            return False
        
        if (word.count(letter) > letterCount):
            return False
            
    return True

#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially
    # 0)
    bestScore = 0

    # Create a new variable to store the best word seen so far (initially None)
    bestWord = None

    # For each word in the wordList
    for word in wordList:
        if (isCompValidWord(word, hand, wordList)):
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to
        # test if the word is in the wordList - you can make a similar function
        # that omits that test)
            
            # Find out how much making that word is worth
            wordScore = getWordScore(word, n)

            # If the score for that word is higher than your best score
            if (wordScore > bestScore):
                # Update your best score, and best word accordingly
                bestScore = wordScore
                bestWord = word

    # return the best word you found.
    return bestWord 

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """

    totalScore = 0
    localHand = dict(hand)
    
    # As long as there are still letters left in the hand:
    while sum(localHand.values()) > 0:

        # Display the hand
        print("Current Hand:"),
        displayHand(localHand)

        # Ask computer for input
        inputWord = compChooseWord(localHand, wordList, n)
        
        # If the input is None:
        if (inputWord == None):
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        
        # If the word is not valid:
        if (not isValidWord(inputWord, localHand, wordList)):
            # Reject invalid word (print a message followed by a blank
            # line)
            print("Invalid word, please try again.")
            print()
            continue

        # Otherwise (the word is valid):

        # Tell the user how many points the word earned, and the
        # updated total score, in one line followed by a blank line
        wordPoints = getWordScore(inputWord, n)
        totalScore += wordPoints
        print ("\"%s\" earned %d points. Total: %d points" % (inputWord, wordPoints, totalScore))
        prin()

        # Update the hand
        #print len(localHand)
        localHand = updateHand(localHand, inputWord)
        #print len(localHand)
        #if len(localHand) == 0:
        #    print "BRAKER!"
        #    break
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the
    # total score
    #if len(localHand) == 0:
    #    print "Run out of letters.  Total score: %d points." % totalScore
    #else:
    print("Total score: %d points." % totalScore)

#    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

    lastHand = {}

    while True:
        userInput = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")

        if userInput == "n":
            lastHand = dealHand(HAND_SIZE)
            choosePlayer(lastHand, wordList, HAND_SIZE)
            
        elif userInput == "r":
            if len(lastHand) == 0:
                print("You have not played a hand yet. Please play a new hand first!")
                continue

            choosePlayer(lastHand, wordList, HAND_SIZE)

        elif userInput == "e":
            break
        else:
            print("Invalid command.")
    
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


