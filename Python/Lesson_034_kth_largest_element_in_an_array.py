# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 034 -- Kth Largest Element In An Array
# Category   : Heap Priority Queue
# Difficulty : Medium
# Study Plan : Day 17
# =============================================================
#
# QUESTION:
#   Given an integer array nums and an integer k, return the kth largest
#   element in the array (the kth largest in sorted order, not the kth
#   distinct element).
#
#   Example:
#     Input : [3,2,1,5,6,4], k=2   Output: 5
# =============================================================

import heapq
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

if __name__ == "__main__":
    print(Solution().findKthLargest([3,2,1,5,6,4], 2))  # 5
