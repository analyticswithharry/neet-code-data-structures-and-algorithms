//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 178 -- Longest Increasing Subsequence
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 89
// =============================================================
//
// QUESTION:
//   Length of the longest strictly-increasing subsequence.
// =============================================================
package main
import ("fmt"; "sort")
func LIS(a []int) int { t:=[]int{}; for _,x:=range a { i:=sort.SearchInts(t,x); if i==len(t) { t=append(t,x) } else { t[i]=x } }; return len(t) }
func main(){ fmt.Println(LIS([]int{10,9,2,5,3,7,101,18})); fmt.Println(LIS([]int{0,1,0,3,2,3})) }
