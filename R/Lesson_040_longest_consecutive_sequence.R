# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 040 -- Longest Consecutive Sequence
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 20
# =============================================================
#
# QUESTION:
#   Given an unsorted array, return the length of the longest consecutive
#   elements sequence in O(n).
#
#   Example: [100,4,200,1,3,2] -> 4 (sequence 1,2,3,4)
# =============================================================

longestConsecutive <- function(nums) {
    s <- unique(nums); best <- 0
    for (n in s) {
        if (!((n-1) %in% s)) {
            cur <- n; len <- 1
            while ((cur+1) %in% s) { cur <- cur+1; len <- len+1 }
            if (len > best) best <- len
        }
    }
    best
}
print(longestConsecutive(c(100,4,200,1,3,2)))
