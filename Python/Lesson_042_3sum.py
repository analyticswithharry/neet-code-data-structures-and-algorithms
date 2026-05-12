# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 042 -- 3Sum
# Category   : Two Pointers
# Difficulty : Medium
# Study Plan : Day 21
# =============================================================
#
# QUESTION:
#   Given nums, return all unique triplets [a,b,c] such that a+b+c=0.
#
#   Example: [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
# =============================================================

class Solution:
    def threeSum(self, nums):
        nums.sort(); res = []
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]: continue
            l, r = i+1, len(nums)-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if s<0: l+=1
                elif s>0: r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]: l+=1
                    while l<r and nums[r]==nums[r-1]: r-=1
                    l+=1; r-=1
        return res

if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4]))
