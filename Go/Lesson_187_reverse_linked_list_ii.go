//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 187 -- Reverse Linked List II
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 94
// =============================================================
//
// QUESTION:
//   Reverse the nodes of the list from position left to right (1-indexed).
// =============================================================
package main
import "fmt"
type N struct{ V int; Nx *N }
func reverseBetween(h *N,L,R int) *N { d:=&N{}; d.Nx=h; pre:=d; for i:=0;i<L-1;i++ { pre=pre.Nx }; cur:=pre.Nx; for i:=0;i<R-L;i++ { nxt:=cur.Nx; cur.Nx=nxt.Nx; nxt.Nx=pre.Nx; pre.Nx=nxt }; return d.Nx }
func main(){ h:=&N{V:1}; c:=h; for _,v:=range []int{2,3,4,5} { c.Nx=&N{V:v}; c=c.Nx }; r:=reverseBetween(h,2,4); for r!=nil { fmt.Print(r.V," "); r=r.Nx }; fmt.Println() }
