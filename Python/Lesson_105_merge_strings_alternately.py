# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 105 -- Merge Strings Alternately
# Category   : Two Pointers
# Difficulty : Easy
# Study Plan : Day 53
# =============================================================
#
# QUESTION:
#   Given two strings, merge them by adding letters in alternating order, starting with word1. If one is longer, append the rest.
# =============================================================

class Solution:
    def mergeAlternately(self, a, b):
        res=[]; i=0
        while i<len(a) or i<len(b):
            if i<len(a): res.append(a[i])
            if i<len(b): res.append(b[i])
            i+=1
        return "".join(res)

if __name__ == "__main__":
    print(Solution().mergeAlternately("abc","pqr"))
    print(Solution().mergeAlternately("ab","pqrs"))
