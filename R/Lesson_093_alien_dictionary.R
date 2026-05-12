# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 093 -- Alien Dictionary
# Category   : Advanced Graphs
# Difficulty : Hard
# Study Plan : Day 47
# =============================================================
#
# QUESTION:
#   Given a sorted list of words from an alien language, derive the order of letters. Return any valid order or '' if impossible.
# =============================================================

alienOrder <- function(words){
  g <- list(); ind <- list()
  for (w in words) for (c in strsplit(w,"")[[1]]){ if(is.null(g[[c]])) g[[c]] <- c(); if(is.null(ind[[c]])) ind[[c]] <- 0 }
  if (length(words) > 1) for (i in 1:(length(words)-1)){
    a <- strsplit(words[i],"")[[1]]; b <- strsplit(words[i+1],"")[[1]]; found <- FALSE
    m <- min(length(a), length(b))
    if (m > 0) for (j in 1:m){
      if (a[j] != b[j]){ if (!(b[j] %in% g[[a[j]]])){ g[[a[j]]] <- c(g[[a[j]]], b[j]); ind[[b[j]]] <- ind[[b[j]]] + 1 }; found <- TRUE; break }
    }
    if (!found && length(a) > length(b)) return("")
  }
  q <- names(ind)[sapply(names(ind), function(c) ind[[c]] == 0)]
  res <- c()
  while (length(q) > 0){
    c <- q[1]; q <- q[-1]; res <- c(res, c)
    for (nx in g[[c]]){ ind[[nx]] <- ind[[nx]] - 1; if (ind[[nx]] == 0) q <- c(q, nx) }
  }
  if (length(res) != length(ind)) return("")
  paste(res, collapse="")
}
print(alienOrder(c("wrt","wrf","er","ett","rftt")))
