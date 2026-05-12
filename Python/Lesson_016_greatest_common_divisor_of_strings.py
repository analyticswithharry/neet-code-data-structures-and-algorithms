# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 016 -- Greatest Common Divisor of Strings
# Category   : Math and Geometry
# Difficulty : Easy
# Study Plan : Day 8
# =============================================================
#
# QUESTION:
#   For two strings s and t, we say "t divides s" if s = t + t + ... + t.
#   Return the largest string x such that x divides both str1 and str2.
#
#   Example:
#     Input : str1="ABCABC", str2="ABC"     Output: "ABC"
#     Input : str1="ABABAB", str2="ABAB"    Output: "AB"
#     Input : str1="LEET",   str2="CODE"    Output: ""
# =============================================================

from math import gcd
class Solution:
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        if s1 + s2 != s2 + s1: return ""
        return s1[:gcd(len(s1), len(s2))]

if __name__ == "__main__":
    s = Solution()
    print(s.gcdOfStrings("ABCABC","ABC"), s.gcdOfStrings("ABABAB","ABAB"), s.gcdOfStrings("LEET","CODE"))
