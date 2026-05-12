# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 186 -- Gas Station
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 93
# =============================================================
#
# QUESTION:
#   Gas[i]/cost[i] arrays around a circular route. Return start index to complete the circuit (or -1).
# =============================================================
def canCompleteCircuit(g,c):
    if sum(g)<sum(c): return -1
    tank=0; start=0
    for i in range(len(g)):
        tank+=g[i]-c[i]
        if tank<0: start=i+1; tank=0
    return start

if __name__=="__main__":
    print(canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
    print(canCompleteCircuit([2,3,4],[3,4,3]))
