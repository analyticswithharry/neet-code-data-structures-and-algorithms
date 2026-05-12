# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 015 -- Excel Sheet Column Title
# Category   : Math and Geometry
# Difficulty : Easy
# Study Plan : Day 8
# =============================================================
#
# QUESTION:
#   Given an integer columnNumber, return its corresponding column title
#   as it appears in an Excel sheet.
#
#   Example:
#     1  -> A
#     28 -> AB
#     701 -> ZY
# =============================================================

class Solution:
    def convertToTitle(self, n: int) -> str:
        out = []
        while n:
            n -= 1
            out.append(chr(ord('A') + n % 26))
            n //= 26
        return "".join(reversed(out))

if __name__ == "__main__":
    print(Solution().convertToTitle(1), Solution().convertToTitle(28), Solution().convertToTitle(701))
