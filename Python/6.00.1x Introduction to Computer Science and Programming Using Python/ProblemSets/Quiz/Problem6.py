def count7(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    
    if (N == 0):
        return 0;

    toAdd = 0

    if (N % 10 == 7):
        toAdd = 1

    return toAdd + count7(N // 10)