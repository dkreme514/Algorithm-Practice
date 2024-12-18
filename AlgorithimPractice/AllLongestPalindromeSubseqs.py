"""
Project: All longest Palindome Subsequence
Descripttion: Given a list, find the longest palindromic 
    subsequence. If there is multiple, return those as well.
    This is found by using dynamic programming. 
    We create a 2D table and fill it using a bottom up approach.
    For subsequence of length one (a single character) stored as palindrom
    For subsequences of length two: sequence is palindromic if they are identical
    For subsequences of length three or more: check if first and last character match,
        we check each first and last character by pulling dp[left+1][right-1].
        Then we continue process and indexing and storingg and incrementing max length.
Author: Donald Kremer 
Date: Fall 2023
"""
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
