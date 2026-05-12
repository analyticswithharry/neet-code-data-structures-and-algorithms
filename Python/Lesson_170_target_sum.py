# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 170 -- Target Sum
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 85
# =============================================================
#
# QUESTION:
#   Assign + or - to each number so the sum equals target. Return number of ways.
# =============================================================
def findTargetSumWays(nums,target):
    from collections import defaultdict
    dp={0:1}
    for n in nums:
        nd=defaultdict(int)
        for s,c in dp.items():
            nd[s+n]+=c; nd[s-n]+=c
        dp=nd
    return dp.get(target,0)

if __name__=="__main__":
    print(findTargetSumWays([1,1,1,1,1],3))
