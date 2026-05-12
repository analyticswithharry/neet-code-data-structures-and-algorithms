//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 189 -- Delete Leaves With a Given Value
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 95
// =============================================================
//
// QUESTION:
//   Delete all leaf nodes with a given target value (cascade).
// =============================================================
package main
import "fmt"
type N struct{ V int; L,R *N }
func rem(n *N,t int) *N { if n==nil { return nil }; n.L=rem(n.L,t); n.R=rem(n.R,t); if n.L==nil && n.R==nil && n.V==t { return nil }; return n }
func show(n *N) string { if n==nil { return "null" }; return fmt.Sprintf("[%d,%s,%s]",n.V,show(n.L),show(n.R)) }
func main(){ r:=&N{V:1,L:&N{V:2,L:&N{V:2}},R:&N{V:3,L:&N{V:2},R:&N{V:4}}}; fmt.Println(show(rem(r,2))) }
