# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 185 -- Jump Game VII
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 93
# =============================================================
#
# QUESTION:
#   Binary string s. Start at 0; can jump from i to any j with i+minJump<=j<=i+maxJump and s[j]='0'. Reach last index?
# =============================================================
canReach <- function(s,mn,mx){ n<-nchar(s); ch<-strsplit(s,"")[[1]]; if(ch[n]!='0'||ch[1]!='0') return(FALSE); pre<-rep(0,n+1); r<-rep(FALSE,n); r[1]<-TRUE; pre[2]<-1; for(i in 2:n){ if(ch[i]=='0'){ lo<-max(0,i-1-mx); hi<-i-1-mn; if(lo<=hi && pre[hi+2]-pre[lo+1]>0) r[i]<-TRUE }; pre[i+1]<-pre[i]+(if(r[i]) 1 else 0) }; r[n] }
cat(canReach("011010",2,3),"\n")
