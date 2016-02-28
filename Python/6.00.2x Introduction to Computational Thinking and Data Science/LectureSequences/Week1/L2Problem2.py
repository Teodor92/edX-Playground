import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    number = random.randint(0, 99)
    
    while (number % 2 == 1):
        number = random.randint(0, 99)
        
    return number