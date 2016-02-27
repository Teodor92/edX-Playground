upperBound = 100;
lowerBound = 0;
midPoint = (upperBound + lowerBound) / 2

print("Please think of a number between 0 and 100!")

while True:
    print("Is your secret number %s?" % str(midPoint))
    palyerInput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if (palyerInput == "l"):
        lowerBound = midPoint;
        midPoint = (upperBound + lowerBound) / 2
    elif (palyerInput == "h"):
        upperBound = midPoint;
        midPoint = (upperBound + lowerBound) / 2
    elif (palyerInput == "c"):
        print("Game over. Your secret number was: %s" % str(midPoint))
        break;
    else:
        print("Sorry, I did not understand your input.")