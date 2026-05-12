# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 092 -- Reorganize String
# Category   : Heap Priority Queue
# Difficulty : Medium
# Study Plan : Day 46
# =============================================================
#
# QUESTION:
#   Given a string s, rearrange so no two adjacent chars are equal. Return the rearranged string, or '' if impossible.
# =============================================================

reorganizeString <- function(s){
  chars <- strsplit(s,"")[[1]]; tab <- table(chars); n <- length(chars)
  if (max(tab) > (n+1) %/% 2 + (n+1) %% 2) {
    if (max(tab) > ceiling(n/2)) return("")
  }
  ord <- names(sort(tab, decreasing=TRUE))
  res <- character(n); i <- 1
  for (ch in ord){
    cnt <- tab[[ch]]
    for (k in 1:cnt){
      if (i > n) i <- 2
      res[i] <- ch; i <- i + 2
    }
  }
  paste(res, collapse="")
}
print(reorganizeString("aab"))
print(paste0("[", reorganizeString("aaab"), "]"))
