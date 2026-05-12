# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 169 -- Coin Change II
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 85
# =============================================================
#
# QUESTION:
#   Number of distinct combinations of coins (unlimited) summing to amount.
# =============================================================
def change(amt,coins):
    dp=[0]*(amt+1); dp[0]=1
    for c in coins:
        for a in range(c,amt+1):
            dp[a]+=dp[a-c]
    return dp[amt]

if __name__=="__main__":
    print(change(5,[1,2,5]))
    print(change(3,[2]))
