//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 020 -- K Closest Points to Origin
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 10
// =============================================================
//
// QUESTION:
//   Given an array of points where points[i] = [xi, yi] and an integer k,
//   return the k closest points to the origin (0, 0). Distance is Euclidean.
//
//   Example:
//     Input : points = [[1,3],[-2,2]], k = 1
//     Output: [[-2,2]]
// =============================================================

package main
import ("fmt"; "sort")
func kClosest(points [][]int, k int) [][]int {
    sort.Slice(points, func(i,j int) bool {
        return points[i][0]*points[i][0]+points[i][1]*points[i][1] <
               points[j][0]*points[j][0]+points[j][1]*points[j][1]
    })
    return points[:k]
}
func main() {
    fmt.Println(kClosest([][]int{{1,3},{-2,2}}, 1))
    fmt.Println(kClosest([][]int{{3,3},{5,-1},{-2,4}}, 2))
}
