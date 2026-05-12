# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 092 -- Reorganize String
# Category   : Heap Priority Queue
# Difficulty : Medium
# Study Plan : Day 46
# =============================================================
#
# QUESTION:
#   Given a string s, rearrange so no two adjacent chars are equal. Return the rearranged string, or '' if impossible.
# =============================================================

import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s):
        cnt = Counter(s); n=len(s)
        if max(cnt.values()) > (n+1)//2: return ""
        h = [(-v,k) for k,v in cnt.items()]; heapq.heapify(h)
        res=[]
        while len(h)>=2:
            v1,c1=heapq.heappop(h); v2,c2=heapq.heappop(h)
            res.append(c1); res.append(c2)
            if v1+1<0: heapq.heappush(h,(v1+1,c1))
            if v2+1<0: heapq.heappush(h,(v2+1,c2))
        if h: res.append(h[0][1])
        return "".join(res)

if __name__ == "__main__":
    print(Solution().reorganizeString("aab"))
    print(Solution().reorganizeString("aaab"))
