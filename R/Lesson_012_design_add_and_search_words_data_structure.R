# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 012 -- Design Add And Search Words Data Structure
# Category   : Tries
# Difficulty : Medium
# Study Plan : Day 6
# =============================================================
#
# QUESTION:
#   Design a data structure that supports:
#     addWord(word)
#     search(word)  - word may contain '.' which matches any single letter
#
#   Example:
#     d = WordDictionary(); d.addWord("bad"); d.addWord("dad"); d.addWord("mad")
#     d.search("pad") -> False
#     d.search("bad") -> True
#     d.search(".ad") -> True
#     d.search("b..") -> True
# =============================================================

new_wd <- function() { e <- new.env(hash=TRUE); e$end <- FALSE; e$ch <- new.env(hash=TRUE); e }
addWord <- function(d, w) {
    n <- d
    for (c in strsplit(w, "")[[1]]) {
        if (!exists(c, envir=n$ch, inherits=FALSE)) assign(c, new_wd(), envir=n$ch)
        n <- get(c, envir=n$ch)
    }
    n$end <- TRUE
}
search_wd <- function(d, w) {
    chars <- strsplit(w, "")[[1]]
    dfs <- function(i, n) {
        if (i > length(chars)) return(n$end)
        c <- chars[i]
        if (c == ".") {
            for (k in ls(n$ch)) if (dfs(i+1, get(k, envir=n$ch))) return(TRUE)
            return(FALSE)
        }
        if (!exists(c, envir=n$ch, inherits=FALSE)) return(FALSE)
        dfs(i+1, get(c, envir=n$ch))
    }
    dfs(1, d)
}

d <- new_wd(); for (w in c("bad","dad","mad")) addWord(d, w)
print(c(search_wd(d,"pad"), search_wd(d,"bad"), search_wd(d,".ad"), search_wd(d,"b..")))
