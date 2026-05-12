# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 089 -- Reconstruct Itinerary
# Category   : Advanced Graphs
# Difficulty : Hard
# Study Plan : Day 45
# =============================================================
#
# QUESTION:
#   Given a list of airline tickets [from,to], reconstruct the itinerary in order, starting from 'JFK'. If multiple valid, return the lexicographically smallest one.
# =============================================================

findItinerary <- function(tickets){
  g <- list()
  for (t in tickets){ a<-t[1]; b<-t[2]; g[[a]] <- c(g[[a]], b) }
  for (k in names(g)) g[[k]] <- sort(g[[k]], decreasing=TRUE)
  st <- c("JFK"); res <- c()
  while (length(st) > 0){
    top <- st[length(st)]
    while (!is.null(g[[top]]) && length(g[[top]]) > 0){
      nxt <- g[[top]][length(g[[top]])]; g[[top]] <- g[[top]][-length(g[[top]])]
      st <- c(st, nxt); top <- nxt
    }
    res <- c(res, st[length(st)]); st <- st[-length(st)]
  }
  rev(res)
}
print(findItinerary(list(c("MUC","LHR"),c("JFK","MUC"),c("SFO","SJC"),c("LHR","SFO"))))
