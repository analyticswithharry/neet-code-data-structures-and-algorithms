//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 049 -- Min Stack
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 24
// =============================================================
//
// QUESTION:
//   Design a stack supporting push, pop, top, and getMin in O(1).
// =============================================================

package main
import "fmt"
type MinStack struct{ s, m []int }
func (st *MinStack) Push(v int){
    st.s = append(st.s, v)
    if len(st.m)==0 || v < st.m[len(st.m)-1] { st.m = append(st.m, v) } else { st.m = append(st.m, st.m[len(st.m)-1]) }
}
func (st *MinStack) Pop(){ st.s = st.s[:len(st.s)-1]; st.m = st.m[:len(st.m)-1] }
func (st *MinStack) Top() int { return st.s[len(st.s)-1] }
func (st *MinStack) GetMin() int { return st.m[len(st.m)-1] }
func main(){
    s := &MinStack{}; s.Push(-2); s.Push(0); s.Push(-3)
    fmt.Println(s.GetMin()); s.Pop(); fmt.Println(s.Top()); fmt.Println(s.GetMin())
}
