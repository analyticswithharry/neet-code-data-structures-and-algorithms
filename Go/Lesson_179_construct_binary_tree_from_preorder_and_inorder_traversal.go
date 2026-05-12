//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 179 -- Construct Binary Tree From Preorder And Inorder Traversal
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 90
// =============================================================
//
// QUESTION:
//   Given preorder and inorder traversals (no duplicates), reconstruct the binary tree.
// =============================================================
package main
import "fmt"
type N struct{ V int; L,R *N }
var P int; var PRE []int; var IDX map[int]int
func rec(lo,hi int) *N { if lo>hi { return nil }; v:=PRE[P]; P++; k:=IDX[v]; n:=&N{V:v}; n.L=rec(lo,k-1); n.R=rec(k+1,hi); return n }
func build(pre,ino []int) *N { P=0; PRE=pre; IDX=map[int]int{}; for i,v:=range ino { IDX[v]=i }; return rec(0,len(ino)-1) }
func pre(n *N,r *[]int){ if n==nil { return }; *r=append(*r,n.V); pre(n.L,r); pre(n.R,r) }
func main(){ t:=build([]int{3,9,20,15,7},[]int{9,3,15,20,7}); var r []int; pre(t,&r); fmt.Println(r) }
