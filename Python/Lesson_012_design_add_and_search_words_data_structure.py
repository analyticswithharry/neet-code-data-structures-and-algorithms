# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 012 -- Design Add And Search Words Data Structure
# Category   : Tries
# Difficulty : Medium
# Study Plan : Day 6
# =============================================================
#
# QUESTION:
#   Design a data structure that supports:
#     addWord(word)
#     search(word)  - word may contain '.' which matches any single letter
#
#   Example:
#     d = WordDictionary(); d.addWord("bad"); d.addWord("dad"); d.addWord("mad")
#     d.search("pad") -> False
#     d.search("bad") -> True
#     d.search(".ad") -> True
#     d.search("b..") -> True
# =============================================================

class WordDictionary:
    def __init__(self):
        self.ch = {}
        self.end = False
    def addWord(self, w):
        n = self
        for c in w: n = n.ch.setdefault(c, WordDictionary())
        n.end = True
    def search(self, w):
        def dfs(i, n):
            if i == len(w): return n.end
            c = w[i]
            if c == '.':
                return any(dfs(i+1, x) for x in n.ch.values())
            return c in n.ch and dfs(i+1, n.ch[c])
        return dfs(0, self)

if __name__ == "__main__":
    d = WordDictionary()
    for w in ["bad","dad","mad"]: d.addWord(w)
    print(d.search("pad"), d.search("bad"), d.search(".ad"), d.search("b.."))
