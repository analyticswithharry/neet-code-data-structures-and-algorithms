# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 086 -- Longest Substring Without Repeating Characters
# Category   : Sliding Window
# Difficulty : Medium
# Study Plan : Day 43
# =============================================================
#
# QUESTION:
#   Given a string s, find the length of the longest substring without repeating characters.
#   Example: 'abcabcbb' -> 3 ('abc'); 'bbbbb' -> 1; 'pwwkew' -> 3.
# =============================================================

class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}; l = 0; best = 0
        for r, c in enumerate(s):
            if c in seen and seen[c] >= l: l = seen[c] + 1
            seen[c] = r
            best = max(best, r - l + 1)
        return best

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
