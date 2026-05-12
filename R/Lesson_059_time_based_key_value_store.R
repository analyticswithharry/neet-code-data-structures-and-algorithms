# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 059 -- Time Based Key Value Store
# Category   : Binary Search
# Difficulty : Medium
# Study Plan : Day 29
# =============================================================
#
# QUESTION:
#   Design a time-based key-value data structure that supports
#   set(key, value, timestamp) and get(key, timestamp), where get returns
#   the value with the largest timestamp <= the given timestamp.
# =============================================================

TimeMap <- function() {
    d <- list()
    list(
        set = function(k, v, t){
            if (is.null(d[[k]])) d[[k]] <<- list(t=integer(), v=character())
            d[[k]]$t <<- c(d[[k]]$t, t); d[[k]]$v <<- c(d[[k]]$v, v)
        },
        get = function(k, t){
            if (is.null(d[[k]])) return("")
            ts <- d[[k]]$t; vs <- d[[k]]$v
            ok <- which(ts <= t)
            if (length(ok)==0) "" else vs[max(ok)]
        }
    )
}
tm <- TimeMap(); tm$set("foo","bar",1)
print(tm$get("foo",1)); print(tm$get("foo",3))
tm$set("foo","bar2",4)
print(tm$get("foo",4)); print(tm$get("foo",5))
