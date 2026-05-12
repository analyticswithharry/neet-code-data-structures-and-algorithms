# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 097 -- Majority Element
# Category   : Arrays and Hashing
# Difficulty : Easy
# Study Plan : Day 49
# =============================================================
#
# QUESTION:
#   Given an array of size n, return the element that appears more than n/2 times.
# =============================================================

class Solution:
    def majorityElement(self, nums):
        cand=0; cnt=0
        for n in nums:
            if cnt==0: cand=n
            cnt += 1 if n==cand else -1
        return cand

if __name__ == "__main__":
    print(Solution().majorityElement([3,2,3]))
    print(Solution().majorityElement([2,2,1,1,1,2,2]))
