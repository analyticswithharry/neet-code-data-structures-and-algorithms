//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 206 -- Number of Connected Components In An Undirected Graph
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 103
// =============================================================
//
// QUESTION:
//   Given n nodes and undirected edges, return the number of connected components.
// =============================================================
package main
import "fmt"
var P []int
func find(x int) int { for P[x]!=x { P[x]=P[P[x]]; x=P[x] }; return x }
func countComponents(n int,e [][]int) int { P=make([]int,n); for i:=range P { P[i]=i }; cnt:=n; for _,x:=range e { ra:=find(x[0]); rb:=find(x[1]); if ra!=rb { P[ra]=rb; cnt-- } }; return cnt }
func main(){ fmt.Println(countComponents(5,[][]int{{0,1},{1,2},{3,4}})) }
