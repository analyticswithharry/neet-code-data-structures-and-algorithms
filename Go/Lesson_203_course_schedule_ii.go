//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 203 -- Course Schedule II
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 102
// =============================================================
//
// QUESTION:
//   Return any topological ordering of courses, or empty array if impossible.
// =============================================================
package main
import "fmt"
func findOrder(n int,pre [][]int) []int { g:=make([][]int,n); ind:=make([]int,n); for _,p:=range pre { g[p[1]]=append(g[p[1]],p[0]); ind[p[0]]++ }; q:=[]int{}; for i:=0;i<n;i++ { if ind[i]==0 { q=append(q,i) } }; res:=[]int{}; for len(q)>0 { x:=q[0]; q=q[1:]; res=append(res,x); for _,y:=range g[x] { ind[y]--; if ind[y]==0 { q=append(q,y) } } }; if len(res)==n { return res }; return []int{} }
func main(){ fmt.Println(findOrder(4,[][]int{{1,0},{2,0},{3,1},{3,2}})) }
