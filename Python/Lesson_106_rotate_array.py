# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 106 -- Rotate Array
# Category   : Two Pointers
# Difficulty : Medium
# Study Plan : Day 53
# =============================================================
#
# QUESTION:
#   Rotate the array to the right by k steps in-place.
# =============================================================

class Solution:
    def rotate(self, nums, k):
        n=len(nums); k%=n
        nums[:] = nums[-k:] + nums[:-k]

if __name__ == "__main__":
    a=[1,2,3,4,5,6,7]; Solution().rotate(a,3); print(a)
