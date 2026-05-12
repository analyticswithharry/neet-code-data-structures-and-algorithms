# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 177 -- Word Break
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 89
# =============================================================
#
# QUESTION:
#   Determine if string s can be segmented into words from the given dictionary.
# =============================================================
wordBreak <- function(s,wd){ w<-as.list(wd); names(w)<-wd; n<-nchar(s); dp<-c(TRUE,rep(FALSE,n)); for(i in 1:n) for(j in 0:(i-1)) if(dp[j+1] && !is.null(w[[substr(s,j+1,i)]])){ dp[i+1]<-TRUE; break }; dp[n+1] }
cat(wordBreak("leetcode",c("leet","code")),"\n")
