# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 016 -- Greatest Common Divisor of Strings
# Category   : Math and Geometry
# Difficulty : Easy
# Study Plan : Day 8
# =============================================================
#
# QUESTION:
#   For two strings s and t, we say "t divides s" if s = t + t + ... + t.
#   Return the largest string x such that x divides both str1 and str2.
#
#   Example:
#     Input : str1="ABCABC", str2="ABC"     Output: "ABC"
#     Input : str1="ABABAB", str2="ABAB"    Output: "AB"
#     Input : str1="LEET",   str2="CODE"    Output: ""
# =============================================================

gcd_int <- function(a,b) { while (b != 0) { t <- b; b <- a %% b; a <- t }; a }
gcdOfStrings <- function(s1, s2) {
    if (paste0(s1,s2) != paste0(s2,s1)) return("")
    substr(s1, 1, gcd_int(nchar(s1), nchar(s2)))
}
print(c(gcdOfStrings("ABCABC","ABC"), gcdOfStrings("ABABAB","ABAB"), gcdOfStrings("LEET","CODE")))
