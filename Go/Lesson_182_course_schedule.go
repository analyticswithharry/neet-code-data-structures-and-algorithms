//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 182 -- Course Schedule
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 91
// =============================================================
//
// QUESTION:
//   Given prerequisites pairs, can all courses be finished (no cycle)?
// =============================================================
package main
import "fmt"
func canFinish(n int,pre [][]int) bool { g:=make([][]int,n); ind:=make([]int,n); for _,p:=range pre { g[p[1]]=append(g[p[1]],p[0]); ind[p[0]]++ }; q:=[]int{}; for i:=0;i<n;i++ { if ind[i]==0 { q=append(q,i) } }; cnt:=0; for len(q)>0 { x:=q[0]; q=q[1:]; cnt++; for _,y:=range g[x] { ind[y]--; if ind[y]==0 { q=append(q,y) } } }; return cnt==n }
func main(){ fmt.Println(canFinish(2,[][]int{{1,0}})); fmt.Println(canFinish(2,[][]int{{1,0},{0,1}})) }
