# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 060 -- Median of Two Sorted Arrays
# Category   : Binary Search
# Difficulty : Hard
# Study Plan : Day 30
# =============================================================
#
# QUESTION:
#   Given two sorted arrays nums1 and nums2, return the median of the
#   combined sorted array. Run in O(log(min(m,n))).
#
#   Example: [1,3], [2] -> 2.0
# =============================================================

class Solution:
    def findMedianSortedArrays(self, a, b):
        if len(a) > len(b): a, b = b, a
        m, n = len(a), len(b); half = (m+n+1)//2
        lo, hi = 0, m
        while lo <= hi:
            i = (lo+hi)//2; j = half - i
            la = a[i-1] if i>0 else float("-inf")
            ra = a[i] if i<m else float("inf")
            lb = b[j-1] if j>0 else float("-inf")
            rb = b[j] if j<n else float("inf")
            if la <= rb and lb <= ra:
                if (m+n) % 2: return float(max(la, lb))
                return (max(la, lb) + min(ra, rb)) / 2.0
            elif la > rb: hi = i-1
            else: lo = i+1
        return 0.0

if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1,3], [2]))
    print(Solution().findMedianSortedArrays([1,2], [3,4]))
