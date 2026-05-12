# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 047 -- Longest Repeating Character Replacement
# Category   : Sliding Window
# Difficulty : Medium
# Study Plan : Day 23
# =============================================================
#
# QUESTION:
#   Given a string s and integer k, you can change at most k characters.
#   Return length of the longest substring with all same characters.
#
#   Example: s="AABABBA", k=1 -> 4
# =============================================================

class Solution:
    def characterReplacement(self, s, k):
        cnt = {}; l = 0; best = 0; mf = 0
        for r,c in enumerate(s):
            cnt[c] = cnt.get(c,0)+1
            mf = max(mf, cnt[c])
            if r - l + 1 - mf > k:
                cnt[s[l]] -= 1; l += 1
            best = max(best, r - l + 1)
        return best

if __name__ == "__main__":
    print(Solution().characterReplacement("AABABBA", 1))
