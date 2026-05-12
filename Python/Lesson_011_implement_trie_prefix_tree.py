# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 011 -- Implement Trie Prefix Tree
# Category   : Tries
# Difficulty : Medium
# Study Plan : Day 6
# =============================================================
#
# QUESTION:
#   Implement the Trie class with:
#     insert(word)        - inserts the word
#     search(word)        - returns true if word is in trie
#     startsWith(prefix)  - returns true if any word starts with prefix
#
#   Example:
#     trie = Trie()
#     trie.insert("apple")
#     trie.search("apple")   -> True
#     trie.search("app")     -> False
#     trie.startsWith("app") -> True
#     trie.insert("app")
#     trie.search("app")     -> True
# =============================================================

class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
    def insert(self, w):
        n = self
        for c in w:
            n = n.children.setdefault(c, Trie())
        n.end = True
    def _walk(self, w):
        n = self
        for c in w:
            if c not in n.children: return None
            n = n.children[c]
        return n
    def search(self, w): n = self._walk(w); return bool(n) and n.end
    def startsWith(self, p): return self._walk(p) is not None

if __name__ == "__main__":
    t = Trie(); t.insert("apple")
    print(t.search("apple"), t.search("app"), t.startsWith("app"))
    t.insert("app"); print(t.search("app"))
