
def howSum (x, numbers, memo={}) : 
    if (x in memo):
        return memo[x]
    if x == 0:
        return []
    if (x < 0):
        return None
    for num in numbers:
        result = howSum((x - num), numbers, memo) 
        if (result != None):
            memo[x] = result + [num]
            return memo[x]
    memo[x] = None
    return None



print(howSum(600, [7,14])) 