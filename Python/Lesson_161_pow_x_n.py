# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 161 -- Pow x n
# Category   : Math and Geometry
# Difficulty : Medium
# Study Plan : Day 81
# =============================================================
#
# QUESTION:
#   Implement pow(x, n) — x raised to the n-th power.
# =============================================================
def myPow(x,n):
    if n<0: x,n=1/x,-n
    r=1.0
    while n:
        if n&1: r*=x
        x*=x; n>>=1
    return r

if __name__=="__main__":
    print(round(myPow(2.0,10),5))
    print(round(myPow(2.1,3),5))
    print(round(myPow(2.0,-2),5))
