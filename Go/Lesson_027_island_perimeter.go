//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 027 -- Island Perimeter
// Category   : Graphs
// Difficulty : Easy
// Study Plan : Day 14
// =============================================================
//
// QUESTION:
//   Given an m x n grid where 1 represents land and 0 water, return the
//   perimeter of the island (the grid is completely surrounded by water and
//   there is exactly one island).
//
//   Example:
//     Input : grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
//     Output: 16
// =============================================================

package main
import "fmt"
func islandPerimeter(g [][]int) int {
    R, C, p := len(g), len(g[0]), 0
    for r := 0; r < R; r++ { for c := 0; c < C; c++ { if g[r][c] == 1 {
        p += 4
        if r > 0 && g[r-1][c] == 1 { p -= 2 }
        if c > 0 && g[r][c-1] == 1 { p -= 2 }
    } } }
    return p
}
func main() { fmt.Println(islandPerimeter([][]int{{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}})) }
