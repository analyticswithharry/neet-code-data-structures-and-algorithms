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

minExtraChar <- function(s, dictionary) {
    words <- dictionary; n <- nchar(s)
    dp <- integer(n+1)
    for (i in seq_len(n)) {
        dp[i+1] <- dp[i] + 1
        for (j in 0:(i-1)) {
            sub <- substr(s, j+1, i)
            if (sub %in% words) dp[i+1] <- min(dp[i+1], dp[j+1])
        }
    }
    dp[n+1]
}
print(minExtraChar("leetscode", c("leet","code","leetcode")))
