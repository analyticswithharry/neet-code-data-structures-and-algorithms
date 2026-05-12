# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 091 -- Single Threaded CPU
# Category   : Heap Priority Queue
# Difficulty : Medium
# Study Plan : Day 46
# =============================================================
#
# QUESTION:
#   You have tasks[i] = [enqueueTime, processingTime]. CPU picks the task with shortest processing time available; ties broken by index. Return order of indices.
# =============================================================

getOrder <- function(tasks){
  n <- length(tasks); idx <- order(sapply(tasks, function(x) x[1]))
  h <- list(); t <- 0; i <- 1; res <- c()
  while (i <= n || length(h) > 0){
    if (length(h)==0) t <- max(t, tasks[[idx[i]]][1])
    while (i <= n && tasks[[idx[i]]][1] <= t){
      h[[length(h)+1]] <- c(tasks[[idx[i]]][2], idx[i]); i <- i+1
    }
    pv <- sapply(h, function(x) x[1]); pi <- sapply(h, function(x) x[2])
    ord <- order(pv, pi); j <- ord[1]
    t <- t + h[[j]][1]; res <- c(res, h[[j]][2]); h[[j]] <- NULL
  }
  res
}
print(getOrder(list(c(1,2),c(2,4),c(3,2),c(4,1))))
