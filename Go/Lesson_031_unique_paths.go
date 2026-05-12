//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 031 -- Unique Paths
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 16
// =============================================================
//
// QUESTION:
//   A robot is on an m x n grid at the top-left. It can only move right or
//   down. How many possible unique paths are there to reach the bottom-right?
//
//   Example:
//     Input : m=3, n=7  Output: 28
//     Input : m=3, n=2  Output: 3
// =============================================================

package main
import "fmt"
func uniquePaths(m, n int) int {
    dp := make([]int, n); for i := range dp { dp[i] = 1 }
    for i := 1; i < m; i++ { for j := 1; j < n; j++ { dp[j] += dp[j-1] } }
    return dp[n-1]
}
func main() { fmt.Println(uniquePaths(3,7), uniquePaths(3,2)) }
