# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 098 -- Sort Colors
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 49
# =============================================================
#
# QUESTION:
#   Sort an array containing only 0, 1, 2 in-place (Dutch national flag).
# =============================================================

class Solution:
    def sortColors(self, nums):
        l, m, r = 0, 0, len(nums)-1
        while m <= r:
            if nums[m]==0: nums[l],nums[m]=nums[m],nums[l]; l+=1; m+=1
            elif nums[m]==2: nums[r],nums[m]=nums[m],nums[r]; r-=1
            else: m+=1

if __name__ == "__main__":
    a=[2,0,2,1,1,0]; Solution().sortColors(a); print(a)
