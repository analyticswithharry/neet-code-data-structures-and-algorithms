# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 197 -- Median of Two Sorted Arrays
# Category   : Binary Search
# Difficulty : Hard
# Study Plan : Day 99
# =============================================================
#
# QUESTION:
#   Find the median of the two sorted arrays in O(log(min(m,n))).
# =============================================================
def findMedianSortedArrays(a,b):
    if len(a)>len(b): a,b=b,a
    m,n=len(a),len(b); lo=0; hi=m
    while lo<=hi:
        i=(lo+hi)//2; j=(m+n+1)//2-i
        Lx=a[i-1] if i>0 else float('-inf')
        Rx=a[i] if i<m else float('inf')
        Ly=b[j-1] if j>0 else float('-inf')
        Ry=b[j] if j<n else float('inf')
        if Lx<=Ry and Ly<=Rx:
            if (m+n)%2: return max(Lx,Ly)
            return (max(Lx,Ly)+min(Rx,Ry))/2
        elif Lx>Ry: hi=i-1
        else: lo=i+1

if __name__=="__main__":
    print(findMedianSortedArrays([1,3],[2]))
    print(findMedianSortedArrays([1,2],[3,4]))
