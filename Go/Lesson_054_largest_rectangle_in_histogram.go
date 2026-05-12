//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 054 -- Largest Rectangle in Histogram
// Category   : Stack
// Difficulty : Hard
// Study Plan : Day 27
// =============================================================
//
// QUESTION:
//   Given heights of bars, find the area of the largest rectangle.
//
//   Example: [2,1,5,6,2,3] -> 10
// =============================================================

package main
import "fmt"
func largestRectangleArea(h []int) int {
    type p struct{ i, v int }
    st := []p{}; best := 0; n := len(h)
    max := func(a,b int) int { if a>b {return a}; return b }
    for i:=0;i<=n;i++ {
        var v int; if i==n { v = 0 } else { v = h[i] }
        start := i
        for len(st)>0 && st[len(st)-1].v > v {
            top := st[len(st)-1]; st = st[:len(st)-1]
            best = max(best, top.v*(i-top.i))
            start = top.i
        }
        st = append(st, p{start, v})
    }
    return best
}
func main(){ fmt.Println(largestRectangleArea([]int{2,1,5,6,2,3})) }
