# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 088 -- Permutations II
# Category   : Backtracking
# Difficulty : Medium
# Study Plan : Day 44
# =============================================================
#
# QUESTION:
#   Given a collection nums of numbers that might contain duplicates, return all possible unique permutations.
#   Example: [1,1,2] -> [[1,1,2],[1,2,1],[2,1,1]].
# =============================================================

class Solution:
    def permuteUnique(self, nums):
        nums.sort(); res=[]; used=[False]*len(nums); cur=[]
        def bt():
            if len(cur)==len(nums): res.append(cur[:]); return
            for i in range(len(nums)):
                if used[i]: continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]: continue
                used[i]=True; cur.append(nums[i]); bt()
                cur.pop(); used[i]=False
        bt(); return res

if __name__ == "__main__":
    print(Solution().permuteUnique([1,1,2]))
