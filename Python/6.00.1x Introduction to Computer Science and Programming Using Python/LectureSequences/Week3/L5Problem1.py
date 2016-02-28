def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = 1.0;
    
    for i in range(0, exp):
        result *= base
        
    return result;