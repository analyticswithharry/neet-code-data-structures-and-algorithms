# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 207 -- Decode String
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 104
# =============================================================
#
# QUESTION:
#   Decode a run-length-style string like "3[a2[c]]" -> "accaccacc".
# =============================================================
decodeString <- function(s){ st<-list(); cur<-""; k<-0; for(ch in strsplit(s,"")[[1]]){ if(ch %in% as.character(0:9)) k<-k*10+as.integer(ch) else if(ch=="["){ st[[length(st)+1]]<-list(pre=cur,k=k); cur<-""; k<-0 } else if(ch=="]"){ f<-st[[length(st)]]; st[[length(st)]]<-NULL; cur<-paste0(f$pre,paste(rep(cur,f$k),collapse="")) } else cur<-paste0(cur,ch) }; cur }
cat(decodeString("3[a]2[bc]"),"\n"); cat(decodeString("3[a2[c]]"),"\n")
