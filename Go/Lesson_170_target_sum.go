//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 170 -- Target Sum
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 85
// =============================================================
//
// QUESTION:
//   Assign + or - to each number so the sum equals target. Return number of ways.
// =============================================================
package main
import "fmt"
func findTargetSumWays(nums []int,target int) int { dp:=map[int]int{0:1}; for _,n:=range nums { nd:=map[int]int{}; for s,c:=range dp { nd[s+n]+=c; nd[s-n]+=c }; dp=nd }; return dp[target] }
func main(){ fmt.Println(findTargetSumWays([]int{1,1,1,1,1},3)) }
