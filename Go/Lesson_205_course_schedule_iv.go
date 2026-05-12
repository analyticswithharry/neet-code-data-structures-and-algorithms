//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 205 -- Course Schedule IV
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 103
// =============================================================
//
// QUESTION:
//   Given prerequisites, answer queries: is course u a (transitive) prerequisite of v?
// =============================================================
package main
import "fmt"
func checkIfPrerequisite(n int,pre,qs [][]int) []bool { r:=make([][]bool,n); for i:=range r { r[i]=make([]bool,n) }; g:=make([][]int,n); ind:=make([]int,n); for _,p:=range pre { g[p[0]]=append(g[p[0]],p[1]); ind[p[1]]++; r[p[0]][p[1]]=true }; q:=[]int{}; for i:=0;i<n;i++ { if ind[i]==0 { q=append(q,i) } }; order:=[]int{}; for len(q)>0 { x:=q[0]; q=q[1:]; order=append(order,x); for _,y:=range g[x] { ind[y]--; if ind[y]==0 { q=append(q,y) } } }; for _,x:=range order { for _,y:=range g[x] { for k:=0;k<n;k++ { if r[k][x] { r[k][y]=true } } } }; out:=[]bool{}; for _,qq:=range qs { out=append(out,r[qq[0]][qq[1]]) }; return out }
func main(){ fmt.Println(checkIfPrerequisite(3,[][]int{{1,2},{1,0},{2,0}},[][]int{{1,0},{1,2}})) }
