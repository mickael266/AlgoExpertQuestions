def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne+=1
        elif secondNum < firstNum:
            current = firstNum -secondNum 
            idxTwo+=1
        else:
            return [firstNum, secondNum]
            
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair