//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 184 -- Missing Number
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 92
// =============================================================
//
// QUESTION:
//   Array contains n distinct numbers from [0,n]. Return the missing one.
// =============================================================
package main
import "fmt"
func missing(a []int) int { x:=len(a); for i,v:=range a { x^=i^v }; return x }
func main(){ fmt.Println(missing([]int{3,0,1})); fmt.Println(missing([]int{9,6,4,2,3,5,7,0,1})) }
