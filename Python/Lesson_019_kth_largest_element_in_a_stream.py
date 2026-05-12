# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 019 -- Kth Largest Element In a Stream
# Category   : Heap Priority Queue
# Difficulty : Easy
# Study Plan : Day 10
# =============================================================
#
# QUESTION:
#   Design a class to find the kth largest element in a stream. Implement:
#     KthLargest(int k, int[] nums)
#     add(val) -> returns the element representing the kth largest in the stream.
#
#   Example:
#     k=3, nums=[4,5,8,2]
#     add(3) -> 4; add(5) -> 5; add(10) -> 5; add(9) -> 8; add(4) -> 8
# =============================================================

import heapq
class KthLargest:
    def __init__(self, k, nums):
        self.k = k; self.h = nums[:]
        heapq.heapify(self.h)
        while len(self.h) > k: heapq.heappop(self.h)
    def add(self, val):
        heapq.heappush(self.h, val)
        if len(self.h) > self.k: heapq.heappop(self.h)
        return self.h[0]

if __name__ == "__main__":
    kl = KthLargest(3, [4,5,8,2])
    print([kl.add(x) for x in [3,5,10,9,4]])  # [4,5,5,8,8]
