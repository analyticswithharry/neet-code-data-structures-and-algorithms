//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 196 -- Trapping Rain Water
// Category   : Two Pointers
// Difficulty : Hard
// Study Plan : Day 98
// =============================================================
//
// QUESTION:
//   Compute total water trapped between bars given heights.
// =============================================================
package main
import "fmt"
func trap(h []int) int { l,r:=0,len(h)-1; lm,rm,res:=0,0,0; for l<r { if h[l]<h[r] { if h[l]>=lm { lm=h[l] } else { res+=lm-h[l] }; l++ } else { if h[r]>=rm { rm=h[r] } else { res+=rm-h[r] }; r-- } }; return res }
func main(){ fmt.Println(trap([]int{0,1,0,2,1,0,1,3,2,1,2,1})) }
