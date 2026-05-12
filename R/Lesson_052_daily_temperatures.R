# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 052 -- Daily Temperatures
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 26
# =============================================================
#
# QUESTION:
#   Given temperatures, for each day return the number of days until a
#   warmer temperature, or 0 if none.
#
#   Example: [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
# =============================================================

dailyTemperatures <- function(t) {
    n <- length(t); res <- rep(0L, n); st <- c()
    for (i in seq_len(n)) {
        while (length(st)>0 && t[st[length(st)]] < t[i]) {
            j <- st[length(st)]; st <- st[-length(st)]; res[j] <- i - j
        }
        st <- c(st, i)
    }
    res
}
print(dailyTemperatures(c(73,74,75,71,69,72,76,73)))
