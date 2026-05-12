# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 088 -- Permutations II
# Category   : Backtracking
# Difficulty : Medium
# Study Plan : Day 44
# =============================================================
#
# QUESTION:
#   Given a collection nums of numbers that might contain duplicates, return all possible unique permutations.
#   Example: [1,1,2] -> [[1,1,2],[1,2,1],[2,1,1]].
# =============================================================

permuteUnique <- function(nums){
  nums <- sort(nums); n <- length(nums); res <- list(); used <- rep(FALSE,n); cur <- c()
  bt <- function(){
    if (length(cur)==n){ res[[length(res)+1]] <<- cur; return() }
    for (i in 1:n){
      if (used[i]) next
      if (i>1 && nums[i]==nums[i-1] && !used[i-1]) next
      used[i] <<- TRUE; cur <<- c(cur, nums[i]); bt()
      cur <<- cur[-length(cur)]; used[i] <<- FALSE
    }
  }
  bt(); res
}
print(permuteUnique(c(1,1,2)))
