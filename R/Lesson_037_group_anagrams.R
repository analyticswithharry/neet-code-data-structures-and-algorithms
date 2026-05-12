# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 037 -- Group Anagrams
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 18
# =============================================================
#
# QUESTION:
#   Given an array of strings strs, group the anagrams together.
#
#   Example: ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"],["tan","nat"],["bat"]]
# =============================================================

groupAnagrams <- function(strs) {
    keys <- sapply(strs, function(s) paste(sort(strsplit(s,"")[[1]]), collapse=""))
    split(strs, keys)
}
print(groupAnagrams(c("eat","tea","tan","ate","nat","bat")))
