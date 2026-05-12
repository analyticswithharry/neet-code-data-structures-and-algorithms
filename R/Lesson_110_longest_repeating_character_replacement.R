# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 110 -- Longest Repeating Character Replacement
# Category   : Sliding Window
# Difficulty : Medium
# Study Plan : Day 55
# =============================================================
#
# QUESTION:
#   Given a string s and integer k, you may change up to k characters. Return length of longest substring with all same characters.
# =============================================================

characterReplacement <- function(s, k){
  chars <- strsplit(s,"")[[1]]; cnt <- list(); l <- 1; mx <- 0; best <- 0
  for (r in seq_along(chars)){
    c <- chars[r]; cnt[[c]] <- ifelse(is.null(cnt[[c]]), 1, cnt[[c]] + 1)
    if (cnt[[c]] > mx) mx <- cnt[[c]]
    while (r - l + 1 - mx > k){
      cl <- chars[l]; cnt[[cl]] <- cnt[[cl]] - 1; l <- l + 1
    }
    if (r - l + 1 > best) best <- r - l + 1
  }
  best
}
print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 1))
