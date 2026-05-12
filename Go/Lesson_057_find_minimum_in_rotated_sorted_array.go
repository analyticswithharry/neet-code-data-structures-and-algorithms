//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 057 -- Find Minimum in Rotated Sorted Array
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 28
// =============================================================
//
// QUESTION:
//   Given a rotated sorted array of unique elements, return its minimum.
//
//   Example: [3,4,5,1,2] -> 1
// =============================================================

package main
import "fmt"
func findMin(nums []int) int {
    l, r := 0, len(nums)-1
    for l < r {
        mid := (l+r)/2
        if nums[mid] > nums[r] { l = mid+1 } else { r = mid }
    }
    return nums[l]
}
func main(){ fmt.Println(findMin([]int{3,4,5,1,2}), findMin([]int{4,5,6,7,0,1,2})) }
