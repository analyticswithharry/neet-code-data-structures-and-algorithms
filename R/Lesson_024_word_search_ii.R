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

# Recursive DFS with a hash set for words.
findWords <- function(board, words) {
    R <- nrow(board); C <- ncol(board)
    out <- character(0)
    dict <- new.env(hash=TRUE); for (w in words) assign(w, TRUE, envir=dict)
    prefix_set <- new.env(hash=TRUE)
    for (w in words) for (i in seq_len(nchar(w))) assign(substr(w,1,i), TRUE, envir=prefix_set)
    visited <- matrix(FALSE, R, C)
    dfs <- function(r, c, path) {
        if (r<1 || r>R || c<1 || c>C || visited[r,c]) return()
        np <- paste0(path, board[r,c])
        if (!exists(np, envir=prefix_set, inherits=FALSE)) return()
        if (exists(np, envir=dict, inherits=FALSE)) out[[length(out)+1]] <<- np
        visited[r,c] <<- TRUE
        for (d in list(c(1,0),c(-1,0),c(0,1),c(0,-1))) dfs(r+d[1], c+d[2], np)
        visited[r,c] <<- FALSE
    }
    for (r in seq_len(R)) for (c in seq_len(C)) dfs(r, c, "")
    sort(unique(out))
}
b <- matrix(c("o","a","a","n",
              "e","t","a","e",
              "i","h","k","r",
              "i","f","l","v"), nrow=4, byrow=TRUE)
print(findWords(b, c("oath","pea","eat","rain")))
