# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 110 -- Longest Repeating Character Replacement
# Category   : Sliding Window
# Difficulty : Medium
# Study Plan : Day 55
# =============================================================
#
# QUESTION:
#   Given a string s and integer k, you may change up to k characters. Return length of longest substring with all same characters.
# =============================================================

class Solution:
    def characterReplacement(self, s, k):
        cnt={}; l=0; mx=0; best=0
        for r,c in enumerate(s):
            cnt[c]=cnt.get(c,0)+1; mx=max(mx, cnt[c])
            if r-l+1 - mx > k:
                cnt[s[l]] -= 1; l += 1
            best=max(best, r-l+1)
        return best

if __name__ == "__main__":
    print(Solution().characterReplacement("ABAB", 2))
    print(Solution().characterReplacement("AABABBA", 1))
