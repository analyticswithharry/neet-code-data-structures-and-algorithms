# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 036 -- Valid Anagram
# Category   : Arrays and Hashing
# Difficulty : Easy
# Study Plan : Day 18
# =============================================================
#
# QUESTION:
#   Given two strings s and t, return true if t is an anagram of s.
#
#   Example: s = "anagram", t = "nagaram" -> true
# =============================================================

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        d = {}
        for c in s: d[c] = d.get(c,0)+1
        for c in t:
            if d.get(c,0)==0: return False
            d[c]-=1
        return True

if __name__ == "__main__":
    print(Solution().isAnagram("anagram","nagaram"))
    print(Solution().isAnagram("rat","car"))
