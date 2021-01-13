
def shortSum (x, numbers, memo={}) : 
    if (x in memo):
        return memo[x]
    if x == 0:
        return []
    if (x < 0):
        return None
    shortestCombination = None
    for num in numbers:
        result = shortSum((x - num), numbers, memo) 
        if (result != None):
            combination = result + [num]
            if (shortestCombination == None or len(combination) < len(shortestCombination)):
                shortestCombination = combination
    memo[x] = shortestCombination
    return memo[x]




print(shortSum(17, [5,3,7,14])) 