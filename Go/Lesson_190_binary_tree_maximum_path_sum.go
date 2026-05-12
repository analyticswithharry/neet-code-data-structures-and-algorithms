//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 190 -- Binary Tree Maximum Path Sum
// Category   : Trees
// Difficulty : Hard
// Study Plan : Day 95
// =============================================================
//
// QUESTION:
//   Path is any sequence of nodes connected by edges (with at least one node). Return the maximum sum.
// =============================================================
package main
import "fmt"
type N struct{ V int; L,R *N }
var RES int
func dfs(n *N) int { if n==nil { return 0 }; l:=dfs(n.L); if l<0 { l=0 }; r:=dfs(n.R); if r<0 { r=0 }; if n.V+l+r>RES { RES=n.V+l+r }; if l>r { return n.V+l }; return n.V+r }
func maxPathSum(r *N) int { RES=-1<<30; dfs(r); return RES }
func main(){ r:=&N{V:-10,L:&N{V:9},R:&N{V:20,L:&N{V:15},R:&N{V:7}}}; fmt.Println(maxPathSum(r)) }
