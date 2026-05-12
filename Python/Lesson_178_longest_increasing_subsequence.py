# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 178 -- Longest Increasing Subsequence
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 89
# =============================================================
#
# QUESTION:
#   Length of the longest strictly-increasing subsequence.
# =============================================================
from bisect import bisect_left
def LIS(a):
    tail=[]
    for x in a:
        i=bisect_left(tail,x)
        if i==len(tail): tail.append(x)
        else: tail[i]=x
    return len(tail)

if __name__=="__main__":
    print(LIS([10,9,2,5,3,7,101,18]))
    print(LIS([0,1,0,3,2,3]))
