# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 047 -- Longest Repeating Character Replacement
# Category   : Sliding Window
# Difficulty : Medium
# Study Plan : Day 23
# =============================================================
#
# QUESTION:
#   Given a string s and integer k, you can change at most k characters.
#   Return length of the longest substring with all same characters.
#
#   Example: s="AABABBA", k=1 -> 4
# =============================================================

characterReplacement <- function(s, k) {
    chars <- strsplit(s,"")[[1]]; cnt <- list(); l <- 1; best <- 0; mf <- 0
    for (r in seq_along(chars)) {
        c <- chars[r]
        cnt[[c]] <- if (is.null(cnt[[c]])) 1 else cnt[[c]] + 1
        if (cnt[[c]] > mf) mf <- cnt[[c]]
        if (r - l + 1 - mf > k) {
            cnt[[chars[l]]] <- cnt[[chars[l]]] - 1
            l <- l + 1
        }
        if (r - l + 1 > best) best <- r - l + 1
    }
    best
}
print(characterReplacement("AABABBA", 1))
