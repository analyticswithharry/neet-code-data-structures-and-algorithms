# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 048 -- Permutation in String
# Category   : Sliding Window
# Difficulty : Medium
# Study Plan : Day 24
# =============================================================
#
# QUESTION:
#   Given s1 and s2, return true if s2 contains a permutation of s1.
#
#   Example: s1="ab", s2="eidbaooo" -> true
# =============================================================

checkInclusion <- function(s1, s2) {
    if (nchar(s1) > nchar(s2)) return(FALSE)
    a <- table(factor(strsplit(s1,"")[[1]], levels=letters))
    n <- nchar(s1)
    for (i in 1:(nchar(s2)-n+1)) {
        sub <- substr(s2, i, i+n-1)
        b <- table(factor(strsplit(sub,"")[[1]], levels=letters))
        if (all(a==b)) return(TRUE)
    }
    FALSE
}
print(checkInclusion("ab","eidbaooo"))
print(checkInclusion("ab","eidboaoo"))
