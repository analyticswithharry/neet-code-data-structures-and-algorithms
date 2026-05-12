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

exist <- function(board, word){
  R <- length(board); C <- length(board[[1]])
  dfs <- function(r,c,i){
    if (i > nchar(word)) return(TRUE)
    if (r<1||r>R||c<1||c>C||board[[r]][c] != substr(word,i,i)) return(FALSE)
    t <- board[[r]][c]; board[[r]][c] <<- "#"
    ok <- dfs(r+1,c,i+1)||dfs(r-1,c,i+1)||dfs(r,c+1,i+1)||dfs(r,c-1,i+1)
    board[[r]][c] <<- t; ok
  }
  for (r in 1:R) for (c in 1:C) if (dfs(r,c,1)) return(TRUE)
  FALSE
}
b <- list(c("A","B","C","E"), c("S","F","C","S"), c("A","D","E","E"))
print(exist(b, "ABCCED"))
