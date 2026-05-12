# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 168 -- Maximum Product Subarray
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 84
# =============================================================
#
# QUESTION:
#   Find a contiguous subarray with the largest product.
# =============================================================
def maxProduct(a):
    mx=mn=res=a[0]
    for v in a[1:]:
        if v<0: mx,mn=mn,mx
        mx=max(v,mx*v); mn=min(v,mn*v)
        res=max(res,mx)
    return res

if __name__=="__main__":
    print(maxProduct([2,3,-2,4]))
    print(maxProduct([-2,0,-1]))
