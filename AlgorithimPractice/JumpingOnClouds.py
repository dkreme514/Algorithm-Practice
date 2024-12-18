INF = 10**5
def jumpingOnCloudsBottomUp(c):

    dp = [0] * len(c)
    dp[1] if c[1] == 0 else INF
    dp[2] if c[2] == 0 else INF

    for i in range(3,len(c)):
        if c[i] ==1:
            dp[i] = INF
        else:
            dp[i] = min(dp[i-1],dp[i-2]) + 1

    return dp[len(c)-1]