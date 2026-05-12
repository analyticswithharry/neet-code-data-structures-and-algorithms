# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 168 -- Maximum Product Subarray
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 84
# =============================================================
#
# QUESTION:
#   Find a contiguous subarray with the largest product.
# =============================================================
maxProduct <- function(a){ mx<-a[1]; mn<-a[1]; res<-a[1]; if(length(a)>=2) for(i in 2:length(a)){ v<-a[i]; if(v<0){ t<-mx; mx<-mn; mn<-t }; mx<-max(v,mx*v); mn<-min(v,mn*v); res<-max(res,mx) }; res }
cat(maxProduct(c(2,3,-2,4)),"\n")
