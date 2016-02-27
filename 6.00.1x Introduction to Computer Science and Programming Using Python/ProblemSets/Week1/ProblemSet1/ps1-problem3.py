bestSquence = s[0]
bestLength = 1
currentSeq = s[0]
currentLen = 1
index = 0

while index < len(s) - 1:
    letter = s[index]
    nextLetter = s[index + 1]
    if(letter <= nextLetter):
        currentSeq += nextLetter
        currentLen += 1
        
        if(currentLen > bestLength):
            bestLength = currentLen
            bestSquence = currentSeq
    else:
        currentSeq = nextLetter
        currentLen = 1

    index += 1
    
print(bestSquence)