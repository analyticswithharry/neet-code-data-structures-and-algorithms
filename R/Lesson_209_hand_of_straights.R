# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 209 -- Hand of Straights
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 105
# =============================================================
#
# QUESTION:
#   Can hand be rearranged into groups of size W of consecutive cards?
# =============================================================
isNStraightHand <- function(h,W){ if(length(h)%%W!=0) return(FALSE); c<-table(h); keys<-as.integer(names(c)); names(c)<-keys; ord<-order(keys); for(i in ord){ x<-keys[i]; cnt<-c[as.character(x)]; if(cnt>0){ for(k in 0:(W-1)){ key<-as.character(x+k); v<-if(is.na(c[key])) 0 else c[key]; if(v<cnt) return(FALSE); c[key]<<-v-cnt } } }; TRUE }
cat(isNStraightHand(c(1,2,3,6,2,3,4,7,8),3),"\n")
