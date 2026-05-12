# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 036 -- Valid Anagram
# Category   : Arrays and Hashing
# Difficulty : Easy
# Study Plan : Day 18
# =============================================================
#
# QUESTION:
#   Given two strings s and t, return true if t is an anagram of s.
#
#   Example: s = "anagram", t = "nagaram" -> true
# =============================================================

isAnagram <- function(s, t) {
    if (nchar(s)!=nchar(t)) return(FALSE)
    a <- sort(strsplit(s,"")[[1]])
    b <- sort(strsplit(t,"")[[1]])
    all(a==b)
}
print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))
