# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 195 -- Boats to Save People
# Category   : Two Pointers
# Difficulty : Medium
# Study Plan : Day 98
# =============================================================
#
# QUESTION:
#   Each boat holds at most 2 people, total weight <= limit. Return min boats.
# =============================================================
def numRescueBoats(p,limit):
    p.sort(); i=0; j=len(p)-1; b=0
    while i<=j:
        if p[i]+p[j]<=limit: i+=1
        j-=1; b+=1
    return b

if __name__=="__main__":
    print(numRescueBoats([1,2],3))
    print(numRescueBoats([3,2,2,1],3))
    print(numRescueBoats([3,5,3,4],5))
