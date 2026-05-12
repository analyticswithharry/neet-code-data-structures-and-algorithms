# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 011 -- Implement Trie Prefix Tree
# Category   : Tries
# Difficulty : Medium
# Study Plan : Day 6
# =============================================================
#
# QUESTION:
#   Implement the Trie class with:
#     insert(word)        - inserts the word
#     search(word)        - returns true if word is in trie
#     startsWith(prefix)  - returns true if any word starts with prefix
#
#   Example:
#     trie = Trie()
#     trie.insert("apple")
#     trie.search("apple")   -> True
#     trie.search("app")     -> False
#     trie.startsWith("app") -> True
#     trie.insert("app")
#     trie.search("app")     -> True
# =============================================================

# Trie implemented as nested environments.
new_trie <- function() { e <- new.env(hash=TRUE); e$end <- FALSE; e$ch <- new.env(hash=TRUE); e }
insert <- function(t, w) {
    n <- t
    for (c in strsplit(w, "")[[1]]) {
        if (!exists(c, envir=n$ch, inherits=FALSE)) assign(c, new_trie(), envir=n$ch)
        n <- get(c, envir=n$ch)
    }
    n$end <- TRUE
}
walk <- function(t, w) {
    n <- t
    for (c in strsplit(w, "")[[1]]) {
        if (!exists(c, envir=n$ch, inherits=FALSE)) return(NULL)
        n <- get(c, envir=n$ch)
    }
    n
}
search_w <- function(t, w) { n <- walk(t, w); !is.null(n) && n$end }
startsWith_t <- function(t, p) { !is.null(walk(t, p)) }

t <- new_trie(); insert(t, "apple")
print(c(search_w(t,"apple"), search_w(t,"app"), startsWith_t(t,"app")))
insert(t, "app"); print(search_w(t,"app"))
