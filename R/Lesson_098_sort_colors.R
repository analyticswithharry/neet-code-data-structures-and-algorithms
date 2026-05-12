# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 098 -- Sort Colors
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 49
# =============================================================
#
# QUESTION:
#   Sort an array containing only 0, 1, 2 in-place (Dutch national flag).
# =============================================================

sortColors <- function(nums){
  l <- 1; m <- 1; r <- length(nums)
  while (m <= r){
    if (nums[m]==0){ tmp<-nums[l]; nums[l]<-nums[m]; nums[m]<-tmp; l<-l+1; m<-m+1
    } else if (nums[m]==2){ tmp<-nums[r]; nums[r]<-nums[m]; nums[m]<-tmp; r<-r-1
    } else { m<-m+1 }
  }
  nums
}
print(sortColors(c(2,0,2,1,1,0)))
