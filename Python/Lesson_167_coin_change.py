# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 167 -- Coin Change
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 84
# =============================================================
#
# QUESTION:
#   Fewest coins needed to make up amount; coins are unlimited. Return -1 if impossible.
# =============================================================
def coinChange(coins,amt):
    INF=float('inf'); dp=[0]+[INF]*amt
    for a in range(1,amt+1):
        for c in coins:
            if c<=a: dp[a]=min(dp[a],dp[a-c]+1)
    return -1 if dp[amt]==INF else dp[amt]

if __name__=="__main__":
    print(coinChange([1,2,5],11))
    print(coinChange([2],3))
