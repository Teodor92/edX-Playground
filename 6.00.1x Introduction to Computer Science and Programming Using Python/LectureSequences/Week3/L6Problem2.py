def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    
    if(len(aTup) == 0): 
        return tuple()

    result = (aTup[0],)

    for i in range(2, len(aTup), 2):
        result += (aTup[i],)

    return result

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))