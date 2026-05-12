# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 024 -- Word Search II
# Category   : Tries
# Difficulty : Hard
# Study Plan : Day 12
# =============================================================
#
# QUESTION:
#   Given an m x n board of characters and a list of strings words, return
#   all words on the board. Each word must be constructed from letters of
#   sequentially adjacent cells (horizontal/vertical). The same cell may not
#   be used more than once in a word.
#
#   Example:
#     board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
#     words=["oath","pea","eat","rain"]
#     Output: ["oath","eat"]
# =============================================================

class Solution:
    def findWords(self, board, words):
        trie = {}
        for w in words:
            n = trie
            for c in w: n = n.setdefault(c, {})
            n['#'] = w
        rows, cols = len(board), len(board[0])
        out = set()
        def dfs(r, c, n):
            ch = board[r][c]
            if ch not in n: return
            nxt = n[ch]
            if '#' in nxt: out.add(nxt['#'])
            board[r][c] = '*'
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '*':
                    dfs(nr, nc, nxt)
            board[r][c] = ch
        for r in range(rows):
            for c in range(cols): dfs(r, c, trie)
        return list(out)

if __name__ == "__main__":
    b = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    print(sorted(Solution().findWords(b, ["oath","pea","eat","rain"])))
