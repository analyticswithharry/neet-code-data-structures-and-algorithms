//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 176 -- Kth Smallest Element In a Bst
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 88
// =============================================================
//
// QUESTION:
//   Return the kth smallest value in a BST (1-indexed).
// =============================================================
package main
import "fmt"
type N struct{ V int; L,R *N }
func kth(r *N,k int) int { st:=[]*N{}; cur:=r; for cur!=nil || len(st)>0 { for cur!=nil { st=append(st,cur); cur=cur.L }; cur=st[len(st)-1]; st=st[:len(st)-1]; k--; if k==0 { return cur.V }; cur=cur.R }; return -1 }
func main(){ r:=&N{V:3,L:&N{V:1,R:&N{V:2}},R:&N{V:4}}; fmt.Println(kth(r,1)); fmt.Println(kth(r,3)) }
