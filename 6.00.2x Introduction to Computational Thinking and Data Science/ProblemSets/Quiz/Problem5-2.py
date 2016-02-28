def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''

    hola = 0
    for i in range(numTrials):
        b = ['r','r','r','r','g','g','g','g']
        choosenBalls = []
        for a in range(3):
          ball = random.choice(b)
          choosenBalls.append(ball)
          b.remove(ball)
        if choosenBalls[0] == choosenBalls[1] and choosenBalls[1] == choosenBalls[2]:
            hola += 1
    return float(hola) / numTrials