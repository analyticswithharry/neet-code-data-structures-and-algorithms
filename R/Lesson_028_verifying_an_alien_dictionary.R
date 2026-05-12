# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 028 -- Verifying An Alien Dictionary
# Category   : Graphs
# Difficulty : Easy
# Study Plan : Day 14
# =============================================================
#
# QUESTION:
#   In an alien language, surprisingly, they also use English lowercase
#   letters but possibly in a different order. Given a sequence of words
#   written in the alien language and the order of the alphabet, return true
#   iff the given words are sorted lexicographically in this alien language.
#
#   Example:
#     Input : words=["hello","leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"
#     Output: true
# =============================================================

isAlienSorted <- function(words, order) {
    chars <- strsplit(order, "")[[1]]
    idx <- setNames(seq_along(chars), chars)
    cmp <- function(a, b) {
        n <- min(nchar(a), nchar(b))
        for (i in seq_len(n)) {
            ia <- idx[[substr(a,i,i)]]; ib <- idx[[substr(b,i,i)]]
            if (ia != ib) return(ia - ib)
        }
        nchar(a) - nchar(b)
    }
    for (w in 2:length(words)) if (cmp(words[w-1], words[w]) > 0) return(FALSE)
    TRUE
}
print(isAlienSorted(c("hello","leetcode"), "hlabcdefgijkmnopqrstuvwxyz"))
