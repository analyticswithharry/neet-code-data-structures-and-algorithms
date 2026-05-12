# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 053 -- Car Fleet
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 26
# =============================================================
#
# QUESTION:
#   Cars at given positions move toward target with given speeds. A car
#   that catches up forms a fleet. Return the number of fleets that arrive.
#
#   Example: target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3] -> 3
# =============================================================

carFleet <- function(target, position, speed) {
    o <- order(position, decreasing=TRUE)
    p <- position[o]; s <- speed[o]; st <- c()
    for (i in seq_along(p)) {
        t <- (target - p[i]) / s[i]
        if (length(st)==0 || t > st[length(st)]) st <- c(st, t)
    }
    length(st)
}
print(carFleet(12, c(10,8,0,5,3), c(2,4,1,1,3)))
