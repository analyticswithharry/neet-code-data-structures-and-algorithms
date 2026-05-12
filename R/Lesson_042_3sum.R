# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 042 -- 3Sum
# Category   : Two Pointers
# Difficulty : Medium
# Study Plan : Day 21
# =============================================================
#
# QUESTION:
#   Given nums, return all unique triplets [a,b,c] such that a+b+c=0.
#
#   Example: [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
# =============================================================

threeSum <- function(nums) {
    nums <- sort(nums); res <- list()
    n <- length(nums)
    for (i in seq_len(n-2)) {
        if (i>1 && nums[i]==nums[i-1]) next
        l <- i+1; r <- n
        while (l<r) {
            s <- nums[i]+nums[l]+nums[r]
            if (s<0) l <- l+1
            else if (s>0) r <- r-1
            else {
                res[[length(res)+1]] <- c(nums[i],nums[l],nums[r])
                while (l<r && nums[l]==nums[l+1]) l <- l+1
                while (l<r && nums[r]==nums[r-1]) r <- r-1
                l <- l+1; r <- r-1
            }
        }
    }
    res
}
print(threeSum(c(-1,0,1,2,-1,-4)))
