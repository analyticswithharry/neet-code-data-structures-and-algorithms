# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 100 -- Palindrome Partitioning
# Category   : Backtracking
# Difficulty : Medium
# Study Plan : Day 50
# =============================================================
#
# QUESTION:
#   Partition string s such that every substring is a palindrome. Return all possible partitions.
# =============================================================

partition <- function(s){
  res <- list(); cur <- c()
  isPal <- function(x){ y <- strsplit(x,"")[[1]]; all(y == rev(y)) }
  bt <- function(i){
    if (i > nchar(s)){ res[[length(res)+1]] <<- cur; return() }
    for (j in i:nchar(s)){
      sub <- substr(s, i, j); if (isPal(sub)){ cur <<- c(cur, sub); bt(j+1); cur <<- cur[-length(cur)] }
    }
  }
  bt(1); res
}
print(partition("aab"))
