//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 044 -- Trapping Rain Water
// Category   : Two Pointers
// Difficulty : Hard
// Study Plan : Day 22
// =============================================================
//
// QUESTION:
//   Given heights, compute how much water can be trapped after raining.
//
//   Example: [0,1,0,2,1,0,1,3,2,1,2,1] -> 6
// =============================================================

package main
import "fmt"
func trap(h []int) int {
    l, r, lm, rm, ans := 0, len(h)-1, 0, 0, 0
    max := func(a,b int) int { if a>b {return a}; return b }
    for l<r {
        if h[l]<h[r] { lm = max(lm,h[l]); ans += lm-h[l]; l++ } else { rm = max(rm,h[r]); ans += rm-h[r]; r-- }
    }
    return ans
}
func main(){ fmt.Println(trap([]int{0,1,0,2,1,0,1,3,2,1,2,1})) }
