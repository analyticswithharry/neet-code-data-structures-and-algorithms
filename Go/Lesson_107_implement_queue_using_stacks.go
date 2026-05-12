//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 107 -- Implement Queue using Stacks
// Category   : Stack
// Difficulty : Easy
// Study Plan : Day 54
// =============================================================
//
// QUESTION:
//   Implement a FIFO queue using only two stacks.
// =============================================================

package main
import "fmt"
type MyQueue struct { a, b []int }
func (q *MyQueue) Push(x int){ q.a = append(q.a, x) }
func (q *MyQueue) Pop() int { q.Peek(); n := len(q.b); x := q.b[n-1]; q.b = q.b[:n-1]; return x }
func (q *MyQueue) Peek() int {
    if len(q.b)==0 { for len(q.a)>0 { n:=len(q.a); q.b=append(q.b, q.a[n-1]); q.a=q.a[:n-1] } }
    return q.b[len(q.b)-1]
}
func (q *MyQueue) Empty() bool { return len(q.a)==0 && len(q.b)==0 }
func main(){ q := &MyQueue{}; q.Push(1); q.Push(2);
    fmt.Println(q.Peek(), q.Pop(), q.Empty()) }
