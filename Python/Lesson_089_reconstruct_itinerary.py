# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 089 -- Reconstruct Itinerary
# Category   : Advanced Graphs
# Difficulty : Hard
# Study Plan : Day 45
# =============================================================
#
# QUESTION:
#   Given a list of airline tickets [from,to], reconstruct the itinerary in order, starting from 'JFK'. If multiple valid, return the lexicographically smallest one.
# =============================================================

import heapq
class Solution:
    def findItinerary(self, tickets):
        g = {}
        for a,b in tickets: g.setdefault(a,[]).append(b)
        for k in g: g[k].sort(reverse=True)
        st=["JFK"]; res=[]
        while st:
            while g.get(st[-1]): st.append(g[st[-1]].pop())
            res.append(st.pop())
        return res[::-1]

if __name__ == "__main__":
    print(Solution().findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
