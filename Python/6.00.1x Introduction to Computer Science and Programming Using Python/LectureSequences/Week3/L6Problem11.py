def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here

    if(len(aDict) == 0):
        return 

    bestKey = ""
    bestValueCount = 0

    for key in aDict:
        valueCount = len(aDict.get(key))

        if(valueCount >= bestValueCount):
            bestValueCount = valueCount
            bestKey = key

    return bestKey