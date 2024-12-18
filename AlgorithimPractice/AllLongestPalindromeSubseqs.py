def AllLongestPalindromeSubseqs(s):
    rows,cols = len(s), len(s)
    dp=[[0] * cols for i in range(rows)]
    answer = ['']*len(s)
    strs = set()

    def init_dp():
        nonlocal s

        for i in range(len(s)):
            dp[i][i] = 1
        for length in range(1, len(s)):
            for left in range(0, len(s)):
                for right in range(left + length, len(s)):
                    if s[left] == s[right]:
                        dp[left][right] = 2 + dp[left + 1][right - 1]
                    else:
                        dp[left][right] = max(dp[left][right - 1], dp[left + 1][right])

    def explore(answer, left, right):
        nonlocal s
        if (left > right or dp[left][right] == 0):
            str = "".join(answer)
            strs.add(str)
            return
        if (s[left]== s[right]):
            answer[left] = answer[right] = s[left]
            explore(answer, left + 1, right-1)
        elif (dp[left][right-1] < dp[left+1][right]):
            explore(answer,left+1,right)
        elif (dp[left][right-1] > dp[left+1][right]):
            explore(answer,left,right-1)
        else:
            explore(answer.copy(), left,right-1)
            explore(answer.copy(),left+1,right)

    init_dp()
    explore(answer,0,len(s)-1)
    return sorted(strs)

print(AllLongestPalindromeSubseqs("agbcdba"))