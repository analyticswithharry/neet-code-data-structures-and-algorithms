# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 108 -- Evaluate Reverse Polish Notation
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 54
# =============================================================
#
# QUESTION:
#   Evaluate an arithmetic expression in Reverse Polish Notation. Operators: +, -, *, /. Division truncates toward zero.
# =============================================================

evalRPN <- function(tokens){
  st <- c()
  for (t in tokens){
    if (t %in% c("+","-","*","/")){
      b <- st[length(st)]; st <- st[-length(st)]
      a <- st[length(st)]; st <- st[-length(st)]
      v <- switch(t, "+"=a+b, "-"=a-b, "*"=a*b, "/"=trunc(a/b))
      st <- c(st, v)
    } else st <- c(st, as.integer(t))
  }
  st[1]
}
print(evalRPN(c("2","1","+","3","*")))
print(evalRPN(c("10","6","9","3","+","-11","*","/","*","17","+","5","+")))
