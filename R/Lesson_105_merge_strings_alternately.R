# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 105 -- Merge Strings Alternately
# Category   : Two Pointers
# Difficulty : Easy
# Study Plan : Day 53
# =============================================================
#
# QUESTION:
#   Given two strings, merge them by adding letters in alternating order, starting with word1. If one is longer, append the rest.
# =============================================================

mergeAlternately <- function(a, b){
  ca <- strsplit(a,"")[[1]]; cb <- strsplit(b,"")[[1]]
  n <- max(length(ca), length(cb)); r <- c()
  for (i in 1:n){
    if (i <= length(ca)) r <- c(r, ca[i])
    if (i <= length(cb)) r <- c(r, cb[i])
  }
  paste(r, collapse="")
}
print(mergeAlternately("abc","pqr")); print(mergeAlternately("ab","pqrs"))
