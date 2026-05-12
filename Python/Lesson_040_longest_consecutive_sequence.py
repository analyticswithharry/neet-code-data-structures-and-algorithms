# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 040 -- Longest Consecutive Sequence
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 20
# =============================================================
#
# QUESTION:
#   Given an unsorted array, return the length of the longest consecutive
#   elements sequence in O(n).
#
#   Example: [100,4,200,1,3,2] -> 4 (sequence 1,2,3,4)
# =============================================================

class Solution:
    def longestConsecutive(self, nums):
        s = set(nums); best = 0
        for n in s:
            if n-1 not in s:
                cur = n; length = 1
                while cur+1 in s: cur+=1; length+=1
                best = max(best, length)
        return best

if __name__ == "__main__":
    print(Solution().longestConsecutive([100,4,200,1,3,2]))
