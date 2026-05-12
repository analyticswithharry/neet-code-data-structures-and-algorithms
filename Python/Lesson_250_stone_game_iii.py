# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 250 -- Stone Game III
# Category   : 1-D Dynamic Programming
# Difficulty : Hard
# Study Plan : Day 125
# =============================================================

def stoneGameIII(s):
    n = len(s)

    # DP[i] = best score difference starting from i
    dp = [0] * (n + 3)  # padding avoids boundary checks

    for i in range(n - 1, -1, -1):
        best = float('-inf')
        take = 0

        for k in range(3):
            if i + k >= n:
                break
            take += s[i + k]
            best = max(best, take - dp[i + k + 1])

        dp[i] = best

    if dp[0] > 0:
        return "Alice"
    elif dp[0] < 0:
        return "Bob"
    else:
        return "Tie"


if __name__ == "__main__":
    print(stoneGameIII([1, 2, 3, 7]))     # Bob
    print(stoneGameIII([1, 2, 3, -9]))    # Alice