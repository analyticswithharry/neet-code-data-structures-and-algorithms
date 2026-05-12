//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 040 -- Longest Consecutive Sequence
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 20
// =============================================================
//
// QUESTION:
//   Given an unsorted array, return the length of the longest consecutive
//   elements sequence in O(n).
//
//   Example: [100,4,200,1,3,2] -> 4 (sequence 1,2,3,4)
// =============================================================

package main
import "fmt"
func longestConsecutive(nums []int) int {
    s := map[int]bool{}
    for _,n := range nums { s[n] = true }
    best := 0
    for n := range s {
        if !s[n-1] {
            cur, l := n, 1
            for s[cur+1] { cur++; l++ }
            if l > best { best = l }
        }
    }
    return best
}
func main(){ fmt.Println(longestConsecutive([]int{100,4,200,1,3,2})) }
