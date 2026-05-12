//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 097 -- Majority Element
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 49
// =============================================================
//
// QUESTION:
//   Given an array of size n, return the element that appears more than n/2 times.
// =============================================================

package main
import "fmt"
func majorityElement(nums []int) int {
    cand, cnt := 0, 0
    for _, n := range nums { if cnt==0 { cand=n }; if n==cand { cnt++ } else { cnt-- } }
    return cand
}
func main(){ fmt.Println(majorityElement([]int{3,2,3}), majorityElement([]int{2,2,1,1,1,2,2})) }
