# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 100 -- Palindrome Partitioning
# Category   : Backtracking
# Difficulty : Medium
# Study Plan : Day 50
# =============================================================
#
# QUESTION:
#   Partition string s such that every substring is a palindrome. Return all possible partitions.
# =============================================================

class Solution:
    def partition(self, s):
        res=[]; cur=[]
        def isPal(x): return x==x[::-1]
        def bt(i):
            if i==len(s): res.append(cur[:]); return
            for j in range(i+1, len(s)+1):
                if isPal(s[i:j]):
                    cur.append(s[i:j]); bt(j); cur.pop()
        bt(0); return res

if __name__ == "__main__":
    print(Solution().partition("aab"))
