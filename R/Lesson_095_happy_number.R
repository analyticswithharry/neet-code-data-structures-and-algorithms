# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 095 -- Happy Number
# Category   : Math and Geometry
# Difficulty : Easy
# Study Plan : Day 48
# =============================================================
#
# QUESTION:
#   A number is happy if repeatedly summing the squares of its digits eventually equals 1. Return true if n is happy.
# =============================================================

isHappy <- function(n){
  seen <- c()
  while (n != 1 && !(n %in% seen)){
    seen <- c(seen, n); s <- 0
    while (n > 0){ d <- n %% 10; s <- s + d*d; n <- n %/% 10 }
    n <- s
  }
  n == 1
}
print(isHappy(19)); print(isHappy(2))
