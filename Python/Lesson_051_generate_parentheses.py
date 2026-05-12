# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 051 -- Generate Parentheses
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 25
# =============================================================
#
# QUESTION:
#   Given n, return all valid combinations of n pairs of parentheses.
#
#   Example: n=3 -> ["((()))","(()())","(())()","()(())","()()()"]
# =============================================================

class Solution:
    def generateParenthesis(self, n):
        res = []
        def bt(cur, o, c):
            if len(cur) == 2*n: res.append(cur); return
            if o < n: bt(cur+"(", o+1, c)
            if c < o: bt(cur+")", o, c+1)
        bt("", 0, 0)
        return res

if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
