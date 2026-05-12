//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 087 -- Subsets II
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 44
// =============================================================
//
// QUESTION:
//   Given an integer array nums that may contain duplicates, return all possible subsets (the power set), without duplicates.
//   Example: [1,2,2] -> [[],[1],[1,2],[1,2,2],[2],[2,2]].
// =============================================================

package main
import ( "fmt"; "sort" )
func subsetsWithDup(nums []int) [][]int {
    sort.Ints(nums); var res [][]int; cur := []int{}
    var bt func(int)
    bt = func(i int){
        tmp := make([]int, len(cur)); copy(tmp, cur); res = append(res, tmp)
        for j := i; j < len(nums); j++ {
            if j > i && nums[j] == nums[j-1] { continue }
            cur = append(cur, nums[j]); bt(j+1); cur = cur[:len(cur)-1]
        }
    }
    bt(0); return res
}
func main(){ fmt.Println(subsetsWithDup([]int{1,2,2})) }
