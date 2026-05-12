# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 023 -- Extra Characters in a String
# Category   : Tries
# Difficulty : Medium
# Study Plan : Day 12
# =============================================================
#
# QUESTION:
#   Given a string s and a dictionary of words, break s into one or more
#   non-overlapping substrings such that each substring is in dictionary.
#   There may be characters in s that are not in any of the substrings.
#   Return the minimum number of extra characters left over.
#
#   Example:
#     Input : s = "leetscode", dict = ["leet","code","leetcode"]
#     Output: 1   (the 's' is extra)
# =============================================================

class Solution:
    def minExtraChar(self, s, dictionary):
        words = set(dictionary); n = len(s)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i-1] + 1
            for j in range(i):
                if s[j:i] in words: dp[i] = min(dp[i], dp[j])
        return dp[n]

if __name__ == "__main__":
    print(Solution().minExtraChar("leetscode", ["leet","code","leetcode"]))  # 1
