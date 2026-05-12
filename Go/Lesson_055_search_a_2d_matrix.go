//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 055 -- Search a 2D Matrix
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 27
// =============================================================
//
// QUESTION:
//   Given an m x n matrix sorted row-wise (and each row's first > prev row's last),
//   search for target.
//
//   Example: [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3 -> true
// =============================================================

package main
import "fmt"
func searchMatrix(m [][]int, target int) bool {
    if len(m)==0 || len(m[0])==0 { return false }
    rows, cols := len(m), len(m[0])
    l, r := 0, rows*cols - 1
    for l <= r {
        mid := (l+r)/2
        v := m[mid/cols][mid%cols]
        if v == target { return true }
        if v < target { l = mid+1 } else { r = mid-1 }
    }
    return false
}
func main(){
    m := [][]int{{1,3,5,7},{10,11,16,20},{23,30,34,60}}
    fmt.Println(searchMatrix(m, 3), searchMatrix(m, 13))
}
