
def canSum (x, numbers, memo={}) :
    if (x in memo):
        return memo[x]
    if x == 0:
        return True
    if (x < 0):
        return False
    for num in numbers:
        if canSum((x - num), numbers, memo) == True:
            memo[x] = True
            return True
    memo[x] = False
    return False



print(canSum(1000, [2,4,7,14])) 