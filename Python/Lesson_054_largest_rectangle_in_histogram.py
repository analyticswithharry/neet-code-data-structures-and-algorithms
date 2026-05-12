# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 054 -- Largest Rectangle in Histogram
# Category   : Stack
# Difficulty : Hard
# Study Plan : Day 27
# =============================================================
#
# QUESTION:
#   Given heights of bars, find the area of the largest rectangle.
#
#   Example: [2,1,5,6,2,3] -> 10
# =============================================================

class Solution:
    def largestRectangleArea(self, h):
        st = []; best = 0
        h2 = h + [0]
        for i,v in enumerate(h2):
            start = i
            while st and st[-1][1] > v:
                idx, height = st.pop()
                best = max(best, height*(i-idx))
                start = idx
            st.append((start, v))
        return best

if __name__ == "__main__":
    print(Solution().largestRectangleArea([2,1,5,6,2,3]))
