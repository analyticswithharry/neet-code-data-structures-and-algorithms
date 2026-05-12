# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 188 -- Design Circular Queue
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 94
# =============================================================
#
# QUESTION:
#   Implement a fixed-size circular queue with enQueue/deQueue/Front/Rear/isEmpty/isFull.
# =============================================================
CQ <- function(k){ a<-rep(0,k); h<-0; c<-0; list(en=function(v){ if(c>=k) return(FALSE); a[((h+c)%%k)+1]<<-v; c<<-c+1; TRUE }, de=function(){ if(c==0) return(FALSE); h<<-(h+1)%%k; c<<-c-1; TRUE }, front=function() if(c==0) -1 else a[h+1], rear=function() if(c==0) -1 else a[((h+c-1)%%k)+1]) }
q<-CQ(3); cat(q$en(1),q$en(2),q$en(3),q$en(4),"\n"); cat(q$rear(),"\n")
