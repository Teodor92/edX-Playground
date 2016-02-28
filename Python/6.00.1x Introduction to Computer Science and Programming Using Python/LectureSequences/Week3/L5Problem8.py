def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    if(aStr == "" or (len(aStr) == 1 and aStr != char)):
        return False

    middleCharIndex = len(aStr) / 2;
    middleChar = aStr[middleCharIndex]

    if (middleChar == char):
        return True
    elif (middleChar < char):
        return isIn(char, aStr[middleCharIndex:])
    else:
        return isIn(char, aStr[:middleCharIndex])