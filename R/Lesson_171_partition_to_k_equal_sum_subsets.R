# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 171 -- Partition to K Equal Sum Subsets
# Category   : Backtracking
# Difficulty : Medium
# Study Plan : Day 86
# =============================================================
#
# QUESTION:
#   Determine if nums can be partitioned into k subsets with equal sum.
# =============================================================
canPartitionKSubsets <- function(nums,k){ s<-sum(nums); if(s%%k!=0) return(FALSE); t<-s/k; nums<-sort(nums,decreasing=TRUE); if(nums[1]>t) return(FALSE); b<-rep(0,k); bt<-function(i){ if(i>length(nums)) return(TRUE); for(j in 1:k){ if(b[j]+nums[i]<=t){ b[j]<<-b[j]+nums[i]; if(bt(i+1)) return(TRUE); b[j]<<-b[j]-nums[i] }; if(b[j]==0) break }; FALSE }; bt(1) }
cat(canPartitionKSubsets(c(4,3,2,3,5,2,1),4),"\n")
