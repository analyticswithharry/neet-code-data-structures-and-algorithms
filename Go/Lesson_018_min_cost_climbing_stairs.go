//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 018 -- Min Cost Climbing Stairs
// Category   : 1-D Dynamic Programming
// Difficulty : Easy
// Study Plan : Day 9
// =============================================================
//
// QUESTION:
//   You are given an integer array cost where cost[i] is the cost of i-th
//   step. Once you pay the cost, you can either climb one or two steps. You
//   can start from index 0 or 1. Return the minimum cost to reach the top.
//
//   Example:
//     Input : cost = [10,15,20]            Output: 15
//     Input : cost = [1,100,1,1,1,100,1,1,100,1]   Output: 6
// =============================================================

package main
import "fmt"
func minCostClimbingStairs(cost []int) int {
    a, b := 0, 0
    for _, c := range cost { t := a; if b < t { t = b }; a = b; b = t + c }
    if a < b { return a }
    return b
}
func main() {
    fmt.Println(minCostClimbingStairs([]int{10,15,20}), minCostClimbingStairs([]int{1,100,1,1,1,100,1,1,100,1}))
}
