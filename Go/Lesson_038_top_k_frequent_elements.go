//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 038 -- Top K Frequent Elements
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 19
// =============================================================
//
// QUESTION:
//   Given an integer array nums and integer k, return the k most frequent elements.
//
//   Example: nums = [1,1,1,2,2,3], k = 2 -> [1,2]
// =============================================================

package main
import ("fmt"; "sort")
func topKFrequent(nums []int, k int) []int {
    c := map[int]int{}
    for _,n := range nums { c[n]++ }
    type p struct{ v,f int }
    a := []p{}
    for v,f := range c { a = append(a, p{v,f}) }
    sort.Slice(a, func(i,j int) bool { return a[i].f > a[j].f })
    r := []int{}
    for i:=0;i<k;i++ { r = append(r, a[i].v) }
    return r
}
func main(){ fmt.Println(topKFrequent([]int{1,1,1,2,2,3}, 2)) }
