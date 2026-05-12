# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 107 -- Implement Queue using Stacks
# Category   : Stack
# Difficulty : Easy
# Study Plan : Day 54
# =============================================================
#
# QUESTION:
#   Implement a FIFO queue using only two stacks.
# =============================================================

MyQueue <- function(){
  a <- c(); b <- c()
  push <- function(x) a <<- c(a, x)
  shift <- function(){ if (length(b)==0){ b <<- rev(a); a <<- c() } }
  pop <- function(){ shift(); x <- b[length(b)]; b <<- b[-length(b)]; x }
  peek <- function(){ shift(); b[length(b)] }
  empty <- function() length(a)==0 && length(b)==0
  list(push=push, pop=pop, peek=peek, empty=empty)
}
q <- MyQueue(); q$push(1); q$push(2); print(q$peek()); print(q$pop()); print(q$empty())
