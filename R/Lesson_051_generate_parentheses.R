# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 051 -- Generate Parentheses
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 25
# =============================================================
#
# QUESTION:
#   Given n, return all valid combinations of n pairs of parentheses.
#
#   Example: n=3 -> ["((()))","(()())","(())()","()(())","()()()"]
# =============================================================

generateParenthesis <- function(n) {
    res <- c()
    bt <- function(cur, o, c) {
        if (nchar(cur) == 2*n) { res[[length(res)+1]] <<- cur; return() }
        if (o < n) bt(paste0(cur,"("), o+1, c)
        if (c < o) bt(paste0(cur,")"), o, c+1)
    }
    bt("", 0, 0)
    res
}
print(generateParenthesis(3))
