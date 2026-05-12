# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 046 -- Longest Substring Without Repeating Characters
# Category   : Sliding Window
# Difficulty : Medium
# Study Plan : Day 23
# =============================================================
#
# QUESTION:
#   Given a string, find the length of the longest substring without
#   repeating characters.
#
#   Example: "abcabcbb" -> 3
# =============================================================

lengthOfLongestSubstring <- function(s) {
    chars <- strsplit(s,"")[[1]]; seen <- list(); l <- 1; best <- 0
    for (r in seq_along(chars)) {
        c <- chars[r]
        if (!is.null(seen[[c]]) && seen[[c]] >= l) l <- seen[[c]] + 1
        seen[[c]] <- r
        if (r - l + 1 > best) best <- r - l + 1
    }
    best
}
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
