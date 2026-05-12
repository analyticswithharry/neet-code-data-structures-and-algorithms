# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 049 -- Min Stack
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 24
# =============================================================
#
# QUESTION:
#   Design a stack supporting push, pop, top, and getMin in O(1).
# =============================================================

MinStack <- function() {
    s <- c(); m <- c()
    list(
        push = function(v){ s <<- c(s, v); m <<- c(m, if (length(m)==0) v else min(v, m[length(m)])) },
        pop  = function(){ s <<- s[-length(s)]; m <<- m[-length(m)] },
        top  = function() s[length(s)],
        getMin = function() m[length(m)]
    )
}
st <- MinStack(); st$push(-2); st$push(0); st$push(-3)
print(st$getMin()); st$pop(); print(st$top()); print(st$getMin())
