# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 048 -- Permutation in String
# Category   : Sliding Window
# Difficulty : Medium
# Study Plan : Day 24
# =============================================================
#
# QUESTION:
#   Given s1 and s2, return true if s2 contains a permutation of s1.
#
#   Example: s1="ab", s2="eidbaooo" -> true
# =============================================================

class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2): return False
        a = [0]*26; b = [0]*26
        for c in s1: a[ord(c)-97]+=1
        for i in range(len(s1)): b[ord(s2[i])-97]+=1
        if a==b: return True
        for i in range(len(s1), len(s2)):
            b[ord(s2[i])-97]+=1
            b[ord(s2[i-len(s1)])-97]-=1
            if a==b: return True
        return False

if __name__ == "__main__":
    print(Solution().checkInclusion("ab","eidbaooo"))
    print(Solution().checkInclusion("ab","eidboaoo"))
