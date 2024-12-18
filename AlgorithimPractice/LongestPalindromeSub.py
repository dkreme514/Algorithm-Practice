
# O(n^2)
def LPS_BU(s):
    rows,cols = len(s),len(s)
    dp=[[0]*cols for _ in range(rows)]

    # Fill out the bottum up table
    for i in range(len(s)):
        dp[i][i]=1
    for length in range(1, len(s)):
        for left in range(0, len(s)):
            #right = length + left
            for right in range(left+length,len(s)):
                if s[left] == s[right]:
                    dp[left][right]= 2 + dp[left+1][right-1]
                else:
                    dp[left][right]= max(dp[left][right-1],dp[left+1][right])
    #lps = dp[0][len(s)-1]
    #return lps



    # O(n)
    # Answer character array initiallizes right and left
    answer = ['']*len(s)
    left,right=0,len(s)-1
    #cycle through comparing values
    while left <= right:
        if s[left]==s[right]:
            answer[left]=answer[right]=s[left]
            left,right = left+1, right+-1
        elif dp[left][right-1] < dp[left+1][right]:
            left+=1
        # If there are two values in the longest, take the smaller one
        elif dp[left][right-1] == dp[left+1][right]:
            if s[left] < s[right]:
                right -=1
            else:
                left +=1
        else:
            right -=1
    s = "".join(answer)

    return s

print(LPS_BU("bacdakdbbhodbvgblkedjglb"))