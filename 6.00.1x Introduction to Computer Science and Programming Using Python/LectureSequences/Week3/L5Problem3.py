def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    
    if (exp == 0):
        return 1

    if (exp % 2 == 0):
        return recurPowerNew((base * base), exp / 2)

    modedExp = exp - 1
    return base * recurPowerNew(base, modedExp)