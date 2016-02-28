# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    result = []
    for trialNumber in range(0, numTrials):
        currentRolls = [];

        for rollNumber in range(0, numRolls):
            currentRolls.append(die.roll())

        result.append(longestRun(currentRolls))

    makeHistogram(result, 10, "NaN", "NaN", "NaN")
    return sum(result) / float(len(result))


def longestRun(L):
    bestRun = []
    currentRun = [L[0]]
    listLength = len(L)

    for i in range(0, listLength - 1):
        if L[i] == L[i + 1]:
            currentRun.append(L[i + 1])
        else:
            if len(currentRun) >= len(bestRun):
                bestRun = list(currentRun)

            currentRun = [L[i + 1]]

    if len(currentRun) >= len(bestRun):
        bestRun = list(currentRun)

    return len(bestRun)