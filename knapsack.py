# unfinished


import math

while True:
    try:
        # m = max weight
        # n = count of items
        m, n = [int(x) for x in input().split()]
        indices = [-1]*(m+1)
        predecessor = [-1]*(m+1)

        # create dp table 
        dp = [[-math.inf]*(m+1)]*(n+1)
        dp[0] = [0]*(m+1)
        for row in dp[1:]:
            row[0] = 0


        for i in range(n):
            value, weight = [int(x) for x in input().split()]

            # if value == 



    except EOFError:
        break