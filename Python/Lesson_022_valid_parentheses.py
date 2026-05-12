# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 022 -- Valid Parentheses
# Category   : Stack
# Difficulty : Easy
# Study Plan : Day 11
# =============================================================
#
# QUESTION:
#   Given a string s containing just the characters '(', ')', '{', '}',
#   '[' and ']', determine if the input string is valid. An input string is
#   valid if open brackets are closed by the same type of brackets in the
#   correct order.
#
#   Example:
#     Input : "()[]{}"   Output: true
#     Input : "(]"       Output: false
# =============================================================

class Solution:
    def isValid(self, s: str) -> bool:
        m = {')':'(', ']':'[', '}':'{'}
        st = []
        for c in s:
            if c in m:
                if not st or st.pop() != m[c]: return False
            else: st.append(c)
        return not st

if __name__ == "__main__":
    print(Solution().isValid("()[]{}"), Solution().isValid("(]"))
