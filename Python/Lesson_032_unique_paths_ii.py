# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 032 -- Unique Paths II
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 16
# =============================================================
#
# QUESTION:
#   You are given an m x n integer array obstacleGrid. There is a robot
#   at the top-left. It moves right or down. An obstacle is marked as 1; an
#   empty space as 0. Return the number of possible unique paths to the
#   bottom-right corner.
#
#   Example:
#     Input : [[0,0,0],[0,1,0],[0,0,0]]   Output: 2
# =============================================================

class Solution:
    def uniquePathsWithObstacles(self, g):
        R, C = len(g), len(g[0])
        if g[0][0] == 1: return 0
        dp = [0] * C; dp[0] = 1
        for r in range(R):
            if g[r][0] == 1: dp[0] = 0
            for c in range(1, C):
                dp[c] = 0 if g[r][c] == 1 else dp[c] + dp[c-1]
        return dp[-1]

if __name__ == "__main__":
    print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))  # 2
