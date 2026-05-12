# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 170 -- Target Sum
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 85
# =============================================================
#
# QUESTION:
#   Assign + or - to each number so the sum equals target. Return number of ways.
# =============================================================
findTargetSumWays <- function(nums,target){ dp<-list(); dp[[as.character(0)]]<-1; for(n in nums){ nd<-list(); for(k in names(dp)){ s<-as.integer(k); v<-dp[[k]]; ka<-as.character(s+n); kb<-as.character(s-n); nd[[ka]]<-(if(is.null(nd[[ka]])) 0 else nd[[ka]])+v; nd[[kb]]<-(if(is.null(nd[[kb]])) 0 else nd[[kb]])+v }; dp<-nd }; v<-dp[[as.character(target)]]; if(is.null(v)) 0 else v }
cat(findTargetSumWays(c(1,1,1,1,1),3),"\n")
