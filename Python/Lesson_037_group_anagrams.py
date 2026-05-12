# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 037 -- Group Anagrams
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 18
# =============================================================
#
# QUESTION:
#   Given an array of strings strs, group the anagrams together.
#
#   Example: ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"],["tan","nat"],["bat"]]
# =============================================================

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)
        return list(d.values())

if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
