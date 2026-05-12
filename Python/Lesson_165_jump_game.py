# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 165 -- Jump Game
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 83
# =============================================================
#
# QUESTION:
#   Each element is max jump length from that position. Return true iff you can reach the last index from index 0.
# =============================================================
def canJump(a):
    r=0
    for i,v in enumerate(a):
        if i>r: return False
        r=max(r,i+v)
    return True

if __name__=="__main__":
    print(canJump([2,3,1,1,4]))
    print(canJump([3,2,1,0,4]))
