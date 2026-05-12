# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 044 -- Trapping Rain Water
# Category   : Two Pointers
# Difficulty : Hard
# Study Plan : Day 22
# =============================================================
#
# QUESTION:
#   Given heights, compute how much water can be trapped after raining.
#
#   Example: [0,1,0,2,1,0,1,3,2,1,2,1] -> 6
# =============================================================

class Solution:
    def trap(self, h):
        l, r = 0, len(h)-1; lm = rm = 0; ans = 0
        while l<r:
            if h[l] < h[r]:
                lm = max(lm, h[l]); ans += lm - h[l]; l+=1
            else:
                rm = max(rm, h[r]); ans += rm - h[r]; r-=1
        return ans

if __name__ == "__main__":
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
