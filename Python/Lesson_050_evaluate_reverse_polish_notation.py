# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 050 -- Evaluate Reverse Polish Notation
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 25
# =============================================================
#
# QUESTION:
#   Evaluate an arithmetic expression in Reverse Polish Notation.
#
#   Example: ["2","1","+","3","*"] -> 9
# =============================================================

class Solution:
    def evalRPN(self, tokens):
        st = []
        for t in tokens:
            if t in "+-*/":
                b = st.pop(); a = st.pop()
                if t=="+": st.append(a+b)
                elif t=="-": st.append(a-b)
                elif t=="*": st.append(a*b)
                else: st.append(int(a/b))
            else: st.append(int(t))
        return st[0]

if __name__ == "__main__":
    print(Solution().evalRPN(["2","1","+","3","*"]))
