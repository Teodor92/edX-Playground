wordToSearchFor = 'bob'

counter = 0;
startIndex = 0;
while True:
    result = s.find(wordToSearchFor, startIndex)
    if result == -1:
        break;
        
    counter += 1;
    
    startIndex = result + len(wordToSearchFor) - 1
    
    
print("Number of times bob occurs is: " + str(counter))