# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 093 -- Alien Dictionary
# Category   : Advanced Graphs
# Difficulty : Hard
# Study Plan : Day 47
# =============================================================
#
# QUESTION:
#   Given a sorted list of words from an alien language, derive the order of letters. Return any valid order or '' if impossible.
# =============================================================

from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words):
        g = defaultdict(set); ind = {c:0 for w in words for c in w}
        for a,b in zip(words, words[1:]):
            for x,y in zip(a,b):
                if x!=y:
                    if y not in g[x]: g[x].add(y); ind[y]+=1
                    break
            else:
                if len(a)>len(b): return ""
        q = deque([c for c in ind if ind[c]==0]); res=[]
        while q:
            c = q.popleft(); res.append(c)
            for nx in g[c]:
                ind[nx]-=1
                if ind[nx]==0: q.append(nx)
        return "".join(res) if len(res)==len(ind) else ""

if __name__ == "__main__":
    print(Solution().alienOrder(["wrt","wrf","er","ett","rftt"]))
