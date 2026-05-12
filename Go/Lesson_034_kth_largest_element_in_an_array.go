//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 034 -- Kth Largest Element In An Array
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 17
// =============================================================
//
// QUESTION:
//   Given an integer array nums and an integer k, return the kth largest
//   element in the array (the kth largest in sorted order, not the kth
//   distinct element).
//
//   Example:
//     Input : [3,2,1,5,6,4], k=2   Output: 5
// =============================================================

package main
import ("fmt"; "sort")
func findKthLargest(nums []int, k int) int {
    a := append([]int{}, nums...)
    sort.Sort(sort.Reverse(sort.IntSlice(a)))
    return a[k-1]
}
func main() { fmt.Println(findKthLargest([]int{3,2,1,5,6,4}, 2)) }
