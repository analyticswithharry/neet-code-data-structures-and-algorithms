# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 053 -- Car Fleet
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 26
# =============================================================
#
# QUESTION:
#   Cars at given positions move toward target with given speeds. A car
#   that catches up forms a fleet. Return the number of fleets that arrive.
#
#   Example: target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3] -> 3
# =============================================================

class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        st = []
        for p,s in cars:
            t = (target - p) / s
            if not st or t > st[-1]: st.append(t)
        return len(st)

if __name__ == "__main__":
    print(Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
