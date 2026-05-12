//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 042 -- 3Sum
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 21
// =============================================================
//
// QUESTION:
//   Given nums, return all unique triplets [a,b,c] such that a+b+c=0.
//
//   Example: [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
// =============================================================

package main
import ("fmt"; "sort")
func threeSum(nums []int) [][]int {
    sort.Ints(nums); res := [][]int{}
    for i:=0; i<len(nums)-2; i++ {
        if i>0 && nums[i]==nums[i-1] { continue }
        l, r := i+1, len(nums)-1
        for l<r {
            s := nums[i]+nums[l]+nums[r]
            if s<0 { l++ } else if s>0 { r-- } else {
                res = append(res, []int{nums[i],nums[l],nums[r]})
                for l<r && nums[l]==nums[l+1] { l++ }
                for l<r && nums[r]==nums[r-1] { r-- }
                l++; r--
            }
        }
    }
    return res
}
func main(){ fmt.Println(threeSum([]int{-1,0,1,2,-1,-4})) }
