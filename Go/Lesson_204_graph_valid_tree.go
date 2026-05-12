//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 204 -- Graph Valid Tree
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 102
// =============================================================
//
// QUESTION:
//   Given n nodes and edges, determine if they form a tree (connected and no cycles).
// =============================================================
package main
import "fmt"
var P []int
func find(x int) int { for P[x]!=x { P[x]=P[P[x]]; x=P[x] }; return x }
func validTree(n int,e [][]int) bool { if len(e)!=n-1 { return false }; P=make([]int,n); for i:=range P { P[i]=i }; for _,x:=range e { ra:=find(x[0]); rb:=find(x[1]); if ra==rb { return false }; P[ra]=rb }; return true }
func main(){ fmt.Println(validTree(5,[][]int{{0,1},{0,2},{0,3},{1,4}})); fmt.Println(validTree(5,[][]int{{0,1},{1,2},{2,3},{1,3},{1,4}})) }
