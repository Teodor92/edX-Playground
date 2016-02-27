def getSublists(L, n):
    currentStart = 0
    result = []
    listLength = len(L)

    while currentStart + n <= listLength:
        sublist = []
        for i in range(currentStart, currentStart + n):
            sublist.append(L[i])

        result.append(sublist)
        currentStart += 1

    return result

print getSublists([10, 4, 6, 8, 3, 4, 5, 7, 7, 2], 4)