# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 099 -- Word Search
# Category   : Backtracking
# Difficulty : Medium
# Study Plan : Day 50
# =============================================================
#
# QUESTION:
#   Given an m x n board and a word, return true if the word exists by sequentially adjacent cells (no reuse).
# =============================================================

class Solution:
    def exist(self, board, word):
        R,C = len(board), len(board[0])
        def dfs(r,c,i):
            if i==len(word): return True
            if r<0 or r>=R or c<0 or c>=C or board[r][c]!=word[i]: return False
            tmp=board[r][c]; board[r][c]='#'
            ok = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            board[r][c]=tmp; return ok
        for r in range(R):
            for c in range(C):
                if dfs(r,c,0): return True
        return False

if __name__ == "__main__":
    print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
