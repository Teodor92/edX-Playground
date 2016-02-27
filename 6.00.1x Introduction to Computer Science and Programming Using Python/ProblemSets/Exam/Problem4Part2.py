def longestRun(L):
    bestRun = []
    currentRun = [L[0]]
    listLength = len(L)

    for i in range(0, listLength - 1):
        if L[i] <= L[i + 1]:
            currentRun.append(L[i + 1])
        #else if i == listLength - 2 and L[i] <= L[i + 1]:
        #    currentRun.append(L[i])
        else:
            #currentRun.append(L[i + 1])
            if len(currentRun) >= len(bestRun):
                bestRun = list(currentRun)

            currentRun = [L[i + 1]]

    if len(currentRun) >= len(bestRun):
        bestRun = list(currentRun)

    return len(bestRun)