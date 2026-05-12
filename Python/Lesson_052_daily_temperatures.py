# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 052 -- Daily Temperatures
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 26
# =============================================================
#
# QUESTION:
#   Given temperatures, for each day return the number of days until a
#   warmer temperature, or 0 if none.
#
#   Example: [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
# =============================================================

class Solution:
    def dailyTemperatures(self, t):
        n = len(t); res = [0]*n; st = []
        for i,v in enumerate(t):
            while st and t[st[-1]] < v:
                j = st.pop(); res[j] = i - j
            st.append(i)
        return res

if __name__ == "__main__":
    print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
