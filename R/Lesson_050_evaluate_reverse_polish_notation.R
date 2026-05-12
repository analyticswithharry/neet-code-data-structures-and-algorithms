# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 050 -- Evaluate Reverse Polish Notation
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 25
# =============================================================
#
# QUESTION:
#   Evaluate an arithmetic expression in Reverse Polish Notation.
#
#   Example: ["2","1","+","3","*"] -> 9
# =============================================================

evalRPN <- function(tokens) {
    st <- c()
    for (t in tokens) {
        if (t %in% c("+","-","*","/")) {
            b <- st[length(st)]; a <- st[length(st)-1]; st <- st[-c(length(st)-1, length(st))]
            r <- switch(t, "+"=a+b, "-"=a-b, "*"=a*b, "/"=as.integer(a/b))
            st <- c(st, r)
        } else st <- c(st, as.integer(t))
    }
    st[1]
}
print(evalRPN(c("2","1","+","3","*")))
