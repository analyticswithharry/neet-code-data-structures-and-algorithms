# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 021 -- Baseball Game
# Category   : Stack
# Difficulty : Easy
# Study Plan : Day 11
# =============================================================
#
# QUESTION:
#   You are keeping the scores for a baseball game. Operations:
#     Integer x : record a new score x
#     '+'       : record sum of previous two scores
#     'D'       : record double of previous score
#     'C'       : invalidate the previous score, removing it
#   Return the sum of all the scores after all operations.
#
#   Example:
#     Input : ops = ["5","2","C","D","+"]
#     Output: 30   (records: 5, 10, 15)
# =============================================================

calPoints <- function(ops) {
    st <- integer(0)
    for (o in ops) {
        if (o == "+") st <- c(st, st[length(st)] + st[length(st)-1])
        else if (o == "D") st <- c(st, 2 * st[length(st)])
        else if (o == "C") st <- st[-length(st)]
        else st <- c(st, as.integer(o))
    }
    sum(st)
}
print(calPoints(c("5","2","C","D","+")))
