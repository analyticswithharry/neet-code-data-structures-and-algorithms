# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 087 -- Subsets II
# Category   : Backtracking
# Difficulty : Medium
# Study Plan : Day 44
# =============================================================
#
# QUESTION:
#   Given an integer array nums that may contain duplicates, return all possible subsets (the power set), without duplicates.
#   Example: [1,2,2] -> [[],[1],[1,2],[1,2,2],[2],[2,2]].
# =============================================================

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort(); res = []; cur = []
        def bt(i):
            res.append(cur[:])
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]: continue
                cur.append(nums[j]); bt(j+1); cur.pop()
        bt(0); return res

if __name__ == "__main__":
    print(Solution().subsetsWithDup([1,2,2]))
