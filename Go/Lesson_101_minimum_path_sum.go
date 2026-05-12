//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 101 -- Minimum Path Sum
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 51
// =============================================================
//
// QUESTION:
//   Given an m x n grid filled with non-negative numbers, find the minimum path sum from top-left to bottom-right (only moves right or down).
// =============================================================

package main
import "fmt"
func minPathSum(g [][]int) int {
    R, C := len(g), len(g[0])
    for i := 0; i < R; i++ { for j := 0; j < C; j++ {
        if i==0 && j==0 { continue }
        if i==0 { g[i][j]+=g[i][j-1]
        } else if j==0 { g[i][j]+=g[i-1][j]
        } else { a, b := g[i-1][j], g[i][j-1]; if a<b { g[i][j]+=a } else { g[i][j]+=b } }
    }}
    return g[R-1][C-1]
}
func main(){ fmt.Println(minPathSum([][]int{{1,3,1},{1,5,1},{4,2,1}})) }
