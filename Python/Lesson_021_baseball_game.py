# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 021 -- Baseball Game
# Category   : Stack
# Difficulty : Easy
# Study Plan : Day 11
# =============================================================
#
# QUESTION:
#   You are keeping the scores for a baseball game. Operations:
#     Integer x : record a new score x
#     '+'       : record sum of previous two scores
#     'D'       : record double of previous score
#     'C'       : invalidate the previous score, removing it
#   Return the sum of all the scores after all operations.
#
#   Example:
#     Input : ops = ["5","2","C","D","+"]
#     Output: 30   (records: 5, 10, 15)
# =============================================================

class Solution:
    def calPoints(self, ops):
        st = []
        for op in ops:
            if op == '+': st.append(st[-1] + st[-2])
            elif op == 'D': st.append(2 * st[-1])
            elif op == 'C': st.pop()
            else: st.append(int(op))
        return sum(st)

if __name__ == "__main__":
    print(Solution().calPoints(["5","2","C","D","+"]))  # 30
