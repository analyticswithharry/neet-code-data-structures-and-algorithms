//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 096 -- Rotate Image
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 48
// =============================================================
//
// QUESTION:
//   Rotate an n x n 2D matrix 90 degrees clockwise in-place.
// =============================================================

package main
import "fmt"
func rotate(m [][]int) {
    n := len(m)
    for i := 0; i < n; i++ { for j := i+1; j < n; j++ { m[i][j], m[j][i] = m[j][i], m[i][j] } }
    for _, r := range m { for i, j := 0, n-1; i < j; i, j = i+1, j-1 { r[i], r[j] = r[j], r[i] } }
}
func main(){ m := [][]int{{1,2,3},{4,5,6},{7,8,9}}; rotate(m); fmt.Println(m) }
