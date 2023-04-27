'''
Solution 1 
#   Time: O(n) Space:O(n)

def firstDuplicateValue(array):
    # Write your code here.
    dict = {}
    for num in array:
        if num not in dict:
            dict[num] = 0
        dict[num] += 1
        
        if dict[num] == 2:
            return num         
        
    
    return -1
'''

#Solution 2

# O(n) time | O(1) space

def firstDuplicateValue(array):
    # Write your code here.
    for num in array:
        absVal = abs(num)
        if array[absVal -1] < 0:
            return absVal
        array[absVal -1 ] *=-1
    return -1