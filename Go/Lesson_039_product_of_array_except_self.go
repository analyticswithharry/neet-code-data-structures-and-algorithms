//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 039 -- Product of Array Except Self
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 19
// =============================================================
//
// QUESTION:
//   Given nums, return an array where answer[i] is the product of all elements
//   except nums[i]. Must run in O(n) without division.
//
//   Example: [1,2,3,4] -> [24,12,8,6]
// =============================================================

package main
import "fmt"
func productExceptSelf(nums []int) []int {
    n := len(nums); r := make([]int, n)
    left := 1
    for i:=0;i<n;i++ { r[i]=left; left*=nums[i] }
    right := 1
    for i:=n-1;i>=0;i-- { r[i]*=right; right*=nums[i] }
    return r
}
func main(){ fmt.Println(productExceptSelf([]int{1,2,3,4})) }
