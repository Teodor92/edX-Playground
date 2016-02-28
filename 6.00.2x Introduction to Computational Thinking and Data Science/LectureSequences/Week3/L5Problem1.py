def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''

    hola=0
    for i in range(numTrials):
        b=['r','r','r','g','g','g']
        for a in range(3):
          ball=random.choice(b)
          b.remove(ball)
        if b[0]==b[1] and b[1]==b[2] and b[2]==b[0]:
            hola=hola+1
    return float(hola)/numTrials  