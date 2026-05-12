# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 039 -- Product of Array Except Self
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 19
# =============================================================
#
# QUESTION:
#   Given nums, return an array where answer[i] is the product of all elements
#   except nums[i]. Must run in O(n) without division.
#
#   Example: [1,2,3,4] -> [24,12,8,6]
# =============================================================

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums); res = [1]*n
        left = 1
        for i in range(n): res[i] = left; left *= nums[i]
        right = 1
        for i in range(n-1,-1,-1): res[i] *= right; right *= nums[i]
        return res

if __name__ == "__main__":
    print(Solution().productExceptSelf([1,2,3,4]))
