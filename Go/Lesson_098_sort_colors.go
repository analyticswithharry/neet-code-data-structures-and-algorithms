//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 098 -- Sort Colors
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 49
// =============================================================
//
// QUESTION:
//   Sort an array containing only 0, 1, 2 in-place (Dutch national flag).
// =============================================================

package main
import "fmt"
func sortColors(nums []int) {
    l, m, r := 0, 0, len(nums)-1
    for m <= r {
        if nums[m]==0 { nums[l], nums[m] = nums[m], nums[l]; l++; m++
        } else if nums[m]==2 { nums[r], nums[m] = nums[m], nums[r]; r--
        } else { m++ }
    }
}
func main(){ a := []int{2,0,2,1,1,0}; sortColors(a); fmt.Println(a) }
