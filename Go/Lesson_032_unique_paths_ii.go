//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 032 -- Unique Paths II
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 16
// =============================================================
//
// QUESTION:
//   You are given an m x n integer array obstacleGrid. There is a robot
//   at the top-left. It moves right or down. An obstacle is marked as 1; an
//   empty space as 0. Return the number of possible unique paths to the
//   bottom-right corner.
//
//   Example:
//     Input : [[0,0,0],[0,1,0],[0,0,0]]   Output: 2
// =============================================================

package main
import "fmt"
func uniquePathsWithObstacles(g [][]int) int {
    R, C := len(g), len(g[0])
    if g[0][0] == 1 { return 0 }
    dp := make([]int, C); dp[0] = 1
    for r := 0; r < R; r++ {
        if g[r][0] == 1 { dp[0] = 0 }
        for c := 1; c < C; c++ { if g[r][c] == 1 { dp[c] = 0 } else { dp[c] += dp[c-1] } }
    }
    return dp[C-1]
}
func main() { fmt.Println(uniquePathsWithObstacles([][]int{{0,0,0},{0,1,0},{0,0,0}})) }
