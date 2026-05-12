//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 180 -- House Robber III
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 90
// =============================================================
//
// QUESTION:
//   Houses arranged as a binary tree; cannot rob two directly-linked houses. Return max amount.
// =============================================================
package main
import "fmt"
type N struct{ V int; L,R *N }
func rec(n *N) (int,int) { if n==nil { return 0,0 }; la,lb:=rec(n.L); ra,rb:=rec(n.R); return n.V+lb+rb, max2(la,lb)+max2(ra,rb) }
func max2(a,b int) int { if a>b { return a }; return b }
func rob(r *N) int { a,b:=rec(r); return max2(a,b) }
func main(){ r:=&N{V:3,L:&N{V:2,R:&N{V:3}},R:&N{V:3,R:&N{V:1}}}; fmt.Println(rob(r)) }
