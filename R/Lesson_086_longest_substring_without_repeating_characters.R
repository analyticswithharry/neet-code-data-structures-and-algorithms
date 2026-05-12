# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 086 -- Longest Substring Without Repeating Characters
# Category   : Sliding Window
# Difficulty : Medium
# Study Plan : Day 43
# =============================================================
#
# QUESTION:
#   Given a string s, find the length of the longest substring without repeating characters.
#   Example: 'abcabcbb' -> 3 ('abc'); 'bbbbb' -> 1; 'pwwkew' -> 3.
# =============================================================

lengthOfLongestSubstring <- function(s){
  chars <- strsplit(s,"")[[1]]; m <- list(); l <- 1; best <- 0
  for (r in seq_along(chars)){
    c <- chars[r]
    if (!is.null(m[[c]]) && m[[c]] >= l) l <- m[[c]] + 1
    m[[c]] <- r
    best <- max(best, r - l + 1)
  }
  best
}
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("pwwkew"))
