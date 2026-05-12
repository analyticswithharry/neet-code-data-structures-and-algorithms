# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 038 -- Top K Frequent Elements
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 19
# =============================================================
#
# QUESTION:
#   Given an integer array nums and integer k, return the k most frequent elements.
#
#   Example: nums = [1,1,1,2,2,3], k = 2 -> [1,2]
# =============================================================

from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        return [x for x,_ in Counter(nums).most_common(k)]

if __name__ == "__main__":
    print(Solution().topKFrequent([1,1,1,2,2,3], 2))
