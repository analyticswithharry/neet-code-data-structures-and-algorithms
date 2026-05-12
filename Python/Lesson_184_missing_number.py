# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 184 -- Missing Number
# Category   : Bit Manipulation
# Difficulty : Easy
# Study Plan : Day 92
# =============================================================
#
# QUESTION:
#   Array contains n distinct numbers from [0,n]. Return the missing one.
# =============================================================
def missing(a):
    x=len(a)
    for i,v in enumerate(a):
        x^=i^v
    return x

if __name__=="__main__":
    print(missing([3,0,1]))
    print(missing([9,6,4,2,3,5,7,0,1]))
