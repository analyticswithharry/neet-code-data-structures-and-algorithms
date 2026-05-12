//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 195 -- Boats to Save People
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 98
// =============================================================
//
// QUESTION:
//   Each boat holds at most 2 people, total weight <= limit. Return min boats.
// =============================================================
package main
import ("fmt"; "sort")
func numRescueBoats(p []int,limit int) int { sort.Ints(p); i,j,b:=0,len(p)-1,0; for i<=j { if p[i]+p[j]<=limit { i++ }; j--; b++ }; return b }
func main(){ fmt.Println(numRescueBoats([]int{3,2,2,1},3)); fmt.Println(numRescueBoats([]int{3,5,3,4},5)) }
