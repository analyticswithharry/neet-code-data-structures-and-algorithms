# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 101 -- Minimum Path Sum
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 51
# =============================================================
#
# QUESTION:
#   Given an m x n grid filled with non-negative numbers, find the minimum path sum from top-left to bottom-right (only moves right or down).
# =============================================================

class Solution:
    def minPathSum(self, g):
        R,C=len(g),len(g[0])
        for i in range(R):
            for j in range(C):
                if i==0 and j==0: continue
                if i==0: g[i][j]+=g[i][j-1]
                elif j==0: g[i][j]+=g[i-1][j]
                else: g[i][j]+=min(g[i-1][j], g[i][j-1])
        return g[-1][-1]

if __name__ == "__main__":
    print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
