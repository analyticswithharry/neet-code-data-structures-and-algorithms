//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 043 -- Container With Most Water
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 21
// =============================================================
//
// QUESTION:
//   Given heights, find two lines that with the x-axis form a container
//   holding the most water. Return the max area.
//
//   Example: [1,8,6,2,5,4,8,3,7] -> 49
// =============================================================

package main
import "fmt"
func maxArea(h []int) int {
    i, j, best := 0, len(h)-1, 0
    min := func(a,b int) int { if a<b {return a}; return b }
    for i<j {
        a := (j-i)*min(h[i],h[j])
        if a > best { best = a }
        if h[i]<h[j] { i++ } else { j-- }
    }
    return best
}
func main(){ fmt.Println(maxArea([]int{1,8,6,2,5,4,8,3,7})) }
