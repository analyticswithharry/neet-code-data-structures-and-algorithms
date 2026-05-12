# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 108 -- Evaluate Reverse Polish Notation
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 54
# =============================================================
#
# QUESTION:
#   Evaluate an arithmetic expression in Reverse Polish Notation. Operators: +, -, *, /. Division truncates toward zero.
# =============================================================

class Solution:
    def evalRPN(self, tokens):
        st=[]
        for t in tokens:
            if t in "+-*/":
                b=st.pop(); a=st.pop()
                if t=='+': st.append(a+b)
                elif t=='-': st.append(a-b)
                elif t=='*': st.append(a*b)
                else: st.append(int(a/b))
            else: st.append(int(t))
        return st[0]

if __name__ == "__main__":
    print(Solution().evalRPN(["2","1","+","3","*"]))
    print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
