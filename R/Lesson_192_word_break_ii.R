# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 192 -- Word Break II
# Category   : Backtracking
# Difficulty : Hard
# Study Plan : Day 96
# =============================================================
#
# QUESTION:
#   Return all sentences obtainable by segmenting s using words from dict.
# =============================================================
wordBreak <- function(s,wd){ w<-as.list(rep(TRUE,length(wd))); names(w)<-wd; memo<-list(); dfs<-function(i){ if(i>nchar(s)) return(list("")); k<-as.character(i); if(!is.null(memo[[k]])) return(memo[[k]]); out<-list(); for(j in i:nchar(s)){ p<-substr(s,i,j); if(!is.null(w[[p]])) for(t in dfs(j+1)) out[[length(out)+1]]<- if(nchar(t)==0) p else paste(p,t) }; memo[[k]]<<-out; out }; dfs(1) }
print(wordBreak("catsanddog",c("cat","cats","and","sand","dog")))
