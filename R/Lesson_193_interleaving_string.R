# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 193 -- Interleaving String
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 97
# =============================================================
#
# QUESTION:
#   Determine whether s3 can be formed by interleaving s1 and s2.
# =============================================================
isInterleave <- function(a,b,c){ if(nchar(a)+nchar(b)!=nchar(c)) return(FALSE); dp<-matrix(FALSE,nchar(a)+1,nchar(b)+1); dp[1,1]<-TRUE; for(i in 1:(nchar(a)+1)) for(j in 1:(nchar(b)+1)){ if(i>1 && substr(a,i-1,i-1)==substr(c,i+j-2,i+j-2)) dp[i,j]<-dp[i,j]||dp[i-1,j]; if(j>1 && substr(b,j-1,j-1)==substr(c,i+j-2,i+j-2)) dp[i,j]<-dp[i,j]||dp[i,j-1] }; dp[nchar(a)+1,nchar(b)+1] }
cat(isInterleave("aabcc","dbbca","aadbbcbcac"),"\n")
