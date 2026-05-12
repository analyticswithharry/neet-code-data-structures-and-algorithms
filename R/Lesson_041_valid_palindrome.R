# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 041 -- Valid Palindrome
# Category   : Two Pointers
# Difficulty : Easy
# Study Plan : Day 20
# =============================================================
#
# QUESTION:
#   Return true if s is a palindrome considering only alphanumeric chars
#   and ignoring case.
#
#   Example: "A man, a plan, a canal: Panama" -> true
# =============================================================

isPalindrome <- function(s) {
    s <- tolower(gsub("[^a-zA-Z0-9]", "", s))
    s == paste(rev(strsplit(s,"")[[1]]), collapse="")
}
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
