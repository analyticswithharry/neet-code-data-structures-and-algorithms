//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 165 -- Jump Game
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 83
// =============================================================
//
// QUESTION:
//   Each element is max jump length from that position. Return true iff you can reach the last index from index 0.
// =============================================================
package main
import "fmt"
func canJump(a []int) bool { r:=0; for i,v:=range a { if i>r { return false }; if i+v>r { r=i+v } }; return true }
func main(){ fmt.Println(canJump([]int{2,3,1,1,4})); fmt.Println(canJump([]int{3,2,1,0,4})) }
