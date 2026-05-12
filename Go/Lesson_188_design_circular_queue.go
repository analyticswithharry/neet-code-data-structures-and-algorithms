//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 188 -- Design Circular Queue
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 94
// =============================================================
//
// QUESTION:
//   Implement a fixed-size circular queue with enQueue/deQueue/Front/Rear/isEmpty/isFull.
// =============================================================
package main
import "fmt"
type CQ struct { a []int; k,h,c int }
func New(k int) *CQ { return &CQ{a:make([]int,k),k:k} }
func (q *CQ) En(v int) bool { if q.c==q.k { return false }; q.a[(q.h+q.c)%q.k]=v; q.c++; return true }
func (q *CQ) De() bool { if q.c==0 { return false }; q.h=(q.h+1)%q.k; q.c--; return true }
func (q *CQ) Front() int { if q.c==0 { return -1 }; return q.a[q.h] }
func (q *CQ) Rear() int { if q.c==0 { return -1 }; return q.a[(q.h+q.c-1)%q.k] }
func main(){ q:=New(3); fmt.Println(q.En(1),q.En(2),q.En(3),q.En(4)); fmt.Println(q.Rear(),q.De(),q.En(4),q.Rear()) }
