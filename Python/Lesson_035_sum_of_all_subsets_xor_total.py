# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 035 -- Sum of All Subsets XOR Total
# Category   : Backtracking
# Difficulty : Easy
# Study Plan : Day 18
# =============================================================
#
# QUESTION:
#   The XOR total of an array is the bitwise XOR of all its elements (or 0
#   if empty). Return the sum of all XOR totals for every subset of nums.
#
#   Example:
#     Input : [1,3]      Output: 6   (subsets: [],[1],[3],[1,3] -> 0+1+3+2 = 6)
#     Input : [5,1,6]    Output: 28
# =============================================================

class Solution:
    def subsetXORSum(self, nums):
        total = 0
        def dfs(i, cur):
            nonlocal total
            if i == len(nums): total += cur; return
            dfs(i+1, cur)
            dfs(i+1, cur ^ nums[i])
        dfs(0, 0)
        return total

if __name__ == "__main__":
    print(Solution().subsetXORSum([1,3]), Solution().subsetXORSum([5,1,6]))
