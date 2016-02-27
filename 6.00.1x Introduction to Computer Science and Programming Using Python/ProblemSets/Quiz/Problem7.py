def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    
    allValues = aDict.values()
    result = [];
    for key, value in aDict.iteritems():
        if allValues.count(value) == 1:
            result.append(key)

    return result