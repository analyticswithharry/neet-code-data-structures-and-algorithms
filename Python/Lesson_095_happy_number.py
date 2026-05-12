# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 095 -- Happy Number
# Category   : Math and Geometry
# Difficulty : Easy
# Study Plan : Day 48
# =============================================================
#
# QUESTION:
#   A number is happy if repeatedly summing the squares of its digits eventually equals 1. Return true if n is happy.
# =============================================================

class Solution:
    def isHappy(self, n):
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            n = sum(int(c)**2 for c in str(n))
        return n==1

if __name__ == "__main__":
    print(Solution().isHappy(19))
    print(Solution().isHappy(2))
