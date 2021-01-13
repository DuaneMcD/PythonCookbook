
### Time = O

def  grid (x,y, memo = {}):
    key = x,y
    if key in memo:
        return memo[key]
    if x | y <= 0:
        return 0
    if (x and y) == 1:
        return 1 
    else:
        memo[key] =  grid(x-1,y, memo) + grid(x,y-1, memo)
        return memo[key]


print(grid(3,3))