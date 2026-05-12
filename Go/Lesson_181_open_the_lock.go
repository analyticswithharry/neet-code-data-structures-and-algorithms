//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 181 -- Open The Lock
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 91
// =============================================================
//
// QUESTION:
//   4-wheel lock starts at '0000'. Each move turns a wheel +/-1. Avoid deadends. Return min moves to reach target or -1.
// =============================================================
package main
import "fmt"
func openLock(dead []string,target string) int { D:=map[string]bool{}; for _,x:=range dead { D[x]=true }; if D["0000"] { return -1 }; if target=="0000" { return 0 }; seen:=map[string]bool{"0000":true}; q:=[]string{"0000"}; d:=0; for len(q)>0 { d++; sz:=len(q); for k:=0;k<sz;k++ { s:=q[0]; q=q[1:]; for i:=0;i<4;i++ { for _,x:=range []int{-1,1} { b:=[]byte(s); b[i]=byte('0'+((int(b[i]-'0')+x+10)%10)); ns:=string(b); if ns==target { return d }; if !seen[ns]&&!D[ns] { seen[ns]=true; q=append(q,ns) } } } } }; return -1 }
func main(){ fmt.Println(openLock([]string{"0201","0101","0102","1212","2002"},"0202")) }
