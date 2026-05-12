# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 022 -- Valid Parentheses
# Category   : Stack
# Difficulty : Easy
# Study Plan : Day 11
# =============================================================
#
# QUESTION:
#   Given a string s containing just the characters '(', ')', '{', '}',
#   '[' and ']', determine if the input string is valid. An input string is
#   valid if open brackets are closed by the same type of brackets in the
#   correct order.
#
#   Example:
#     Input : "()[]{}"   Output: true
#     Input : "(]"       Output: false
# =============================================================

isValid <- function(s) {
    m <- c(")"="(", "]"="[", "}"="{")
    st <- character(0)
    for (c in strsplit(s, "")[[1]]) {
        if (c %in% names(m)) {
            if (length(st)==0 || st[length(st)] != m[[c]]) return(FALSE)
            st <- st[-length(st)]
        } else st <- c(st, c)
    }
    length(st) == 0
}
print(c(isValid("()[]{}"), isValid("(]")))
