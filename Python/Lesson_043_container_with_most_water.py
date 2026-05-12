# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 043 -- Container With Most Water
# Category   : Two Pointers
# Difficulty : Medium
# Study Plan : Day 21
# =============================================================
#
# QUESTION:
#   Given heights, find two lines that with the x-axis form a container
#   holding the most water. Return the max area.
#
#   Example: [1,8,6,2,5,4,8,3,7] -> 49
# =============================================================

class Solution:
    def maxArea(self, h):
        i, j, best = 0, len(h)-1, 0
        while i<j:
            best = max(best, (j-i)*min(h[i],h[j]))
            if h[i] < h[j]: i+=1
            else: j-=1
        return best

if __name__ == "__main__":
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
