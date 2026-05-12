# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 087 -- Subsets II
# Category   : Backtracking
# Difficulty : Medium
# Study Plan : Day 44
# =============================================================
#
# QUESTION:
#   Given an integer array nums that may contain duplicates, return all possible subsets (the power set), without duplicates.
#   Example: [1,2,2] -> [[],[1],[1,2],[1,2,2],[2],[2,2]].
# =============================================================

subsetsWithDup <- function(nums){
  nums <- sort(nums); res <- list(); cur <- c()
  bt <- function(i){
    res[[length(res)+1]] <<- cur
    j <- i
    while (j <= length(nums)){
      if (j > i && nums[j] == nums[j-1]) { j <- j+1; next }
      cur <<- c(cur, nums[j]); bt(j+1); cur <<- cur[-length(cur)]
      j <- j+1
    }
  }
  bt(1); res
}
print(subsetsWithDup(c(1,2,2)))
