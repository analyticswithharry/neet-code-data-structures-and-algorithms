# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 162 -- Multiply Strings
# Category   : Math and Geometry
# Difficulty : Medium
# Study Plan : Day 81
# =============================================================
#
# QUESTION:
#   Given two non-negative integers as strings, return their product as a string. Do not use built-in big-int conversion.
# =============================================================
def mul(a,b):
    if a=="0" or b=="0": return "0"
    n,m=len(a),len(b); r=[0]*(n+m)
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            p=int(a[i])*int(b[j])
            s=p+r[i+j+1]
            r[i+j+1]=s%10
            r[i+j]+=s//10
    s="".join(map(str,r)).lstrip("0")
    return s or "0"

if __name__=="__main__":
    print(mul("123","456"))
