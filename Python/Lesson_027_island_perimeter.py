# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 027 -- Island Perimeter
# Category   : Graphs
# Difficulty : Easy
# Study Plan : Day 14
# =============================================================
#
# QUESTION:
#   Given an m x n grid where 1 represents land and 0 water, return the
#   perimeter of the island (the grid is completely surrounded by water and
#   there is exactly one island).
#
#   Example:
#     Input : grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
#     Output: 16
# =============================================================

class Solution:
    def islandPerimeter(self, grid):
        R, C = len(grid), len(grid[0])
        p = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    p += 4
                    if r and grid[r-1][c] == 1: p -= 2
                    if c and grid[r][c-1] == 1: p -= 2
        return p

if __name__ == "__main__":
    print(Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))  # 16
