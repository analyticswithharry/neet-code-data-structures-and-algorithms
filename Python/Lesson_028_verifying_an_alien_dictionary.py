# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 028 -- Verifying An Alien Dictionary
# Category   : Graphs
# Difficulty : Easy
# Study Plan : Day 14
# =============================================================
#
# QUESTION:
#   In an alien language, surprisingly, they also use English lowercase
#   letters but possibly in a different order. Given a sequence of words
#   written in the alien language and the order of the alphabet, return true
#   iff the given words are sorted lexicographically in this alien language.
#
#   Example:
#     Input : words=["hello","leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"
#     Output: true
# =============================================================

class Solution:
    def isAlienSorted(self, words, order):
        idx = {c: i for i, c in enumerate(order)}
        for a, b in zip(words, words[1:]):
            for ca, cb in zip(a, b):
                if idx[ca] != idx[cb]:
                    if idx[ca] > idx[cb]: return False
                    break
            else:
                if len(a) > len(b): return False
        return True

if __name__ == "__main__":
    print(Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
