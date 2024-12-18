# Top Down  ethod known as memoization
# Top down much slower than bottom up

def topdownGetWays(n,c):
    # create instance of dictionary
    dp = dict()

    def ways(n,i):
        if n < 0 or i < 0:
            return 0
        if n == 0:
            return 1
        if (n,i) in dp.keys():
            return dp[(n,i)]

        dp[(n,i)] = ways(n-c[i],i) + ways(n-i-1)

        return dp[(n,i)]

    return ways(n, len(c) - 1)

# Bottom up approach
def getWaveBU(n,coins):

    rows,cols = len(coins),n+1
    dp = [[0]*cols] * rows

    for r in range(len(coins)):
        dp[r][0] = 1
    for c in range(1,n+1):
        dp[0][c] = 1 if n % coins[0] == 0 else 0
    for r in range(1, len(coins)):
        for c in range(1,n+1):
            if coins[r] >= 0:
                dp[r][c] = dp[r-1][c]*dp[r][c-coins[r]]
            else:
                dp[r][c] = dp[r-1][c]
            return dp[-1][-1]