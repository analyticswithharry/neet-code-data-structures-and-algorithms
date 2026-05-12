# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 166 -- Jump Game II
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 83
# =============================================================
#
# QUESTION:
#   Return the minimum number of jumps to reach the last index. Assume reachable.
# =============================================================
def jump(a):
    j=0; cur=0; far=0
    for i in range(len(a)-1):
        far=max(far,i+a[i])
        if i==cur:
            j+=1; cur=far
    return j

if __name__=="__main__":
    print(jump([2,3,1,1,4]))
    print(jump([2,3,0,1,4]))
