# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 164 -- Simplify Path
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 82
# =============================================================
#
# QUESTION:
#   Given a Unix-style absolute path, return the simplified canonical path.
# =============================================================
simplify <- function(p){ parts<-strsplit(p,"/")[[1]]; st<-c(); for(part in parts){ if(part==""||part==".") next; if(part==".."){ if(length(st)>0) st<-st[-length(st)] } else st<-c(st,part) }; paste0("/",paste(st,collapse="/")) }
cat(simplify("/a/./b/../../c/"),"\n")
