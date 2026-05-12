# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 096 -- Rotate Image
# Category   : Math and Geometry
# Difficulty : Medium
# Study Plan : Day 48
# =============================================================
#
# QUESTION:
#   Rotate an n x n 2D matrix 90 degrees clockwise in-place.
# =============================================================

class Solution:
    def rotate(self, m):
        n=len(m)
        for i in range(n):
            for j in range(i+1,n): m[i][j], m[j][i] = m[j][i], m[i][j]
        for row in m: row.reverse()

if __name__ == "__main__":
    m=[[1,2,3],[4,5,6],[7,8,9]]; Solution().rotate(m); print(m)
