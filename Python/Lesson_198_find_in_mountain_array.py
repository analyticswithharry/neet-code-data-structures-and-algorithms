# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 198 -- Find in Mountain Array
# Category   : Binary Search
# Difficulty : Hard
# Study Plan : Day 99
# =============================================================
#
# QUESTION:
#   Mountain array: strictly increasing then strictly decreasing. Return min index with value=target.
# =============================================================
def findInMountainArray(target,a):
    lo,hi=0,len(a)-1
    while lo<hi:
        m=(lo+hi)//2
        if a[m]<a[m+1]: lo=m+1
        else: hi=m
    peak=lo
    def bs(l,r,asc):
        while l<=r:
            m=(l+r)//2
            v=a[m]
            if v==target: return m
            if asc:
                if v<target: l=m+1
                else: r=m-1
            else:
                if v>target: l=m+1
                else: r=m-1
        return -1
    i=bs(0,peak,True)
    if i!=-1: return i
    return bs(peak+1,len(a)-1,False)

if __name__=="__main__":
    print(findInMountainArray(3,[1,2,3,4,5,3,1]))
    print(findInMountainArray(3,[0,1,2,4,2,1]))
