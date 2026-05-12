//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 175 -- Validate Binary Search Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 88
// =============================================================
//
// QUESTION:
//   Determine if a binary tree is a valid BST.
// =============================================================
package main
import ("fmt"; "math")
type N struct{ V int; L,R *N }
func rec(n *N,lo,hi float64) bool { if n==nil { return true }; v:=float64(n.V); if v<=lo||v>=hi { return false }; return rec(n.L,lo,v) && rec(n.R,v,hi) }
func isValidBST(r *N) bool { return rec(r,math.Inf(-1),math.Inf(1)) }
func main(){ r:=&N{V:2,L:&N{V:1},R:&N{V:3}}; fmt.Println(isValidBST(r)) }
