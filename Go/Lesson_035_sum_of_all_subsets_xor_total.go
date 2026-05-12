//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 035 -- Sum of All Subsets XOR Total
// Category   : Backtracking
// Difficulty : Easy
// Study Plan : Day 18
// =============================================================
//
// QUESTION:
//   The XOR total of an array is the bitwise XOR of all its elements (or 0
//   if empty). Return the sum of all XOR totals for every subset of nums.
//
//   Example:
//     Input : [1,3]      Output: 6   (subsets: [],[1],[3],[1,3] -> 0+1+3+2 = 6)
//     Input : [5,1,6]    Output: 28
// =============================================================

package main
import "fmt"
func subsetXORSum(nums []int) int {
    total := 0
    var dfs func(i, cur int)
    dfs = func(i, cur int) {
        if i == len(nums) { total += cur; return }
        dfs(i+1, cur); dfs(i+1, cur ^ nums[i])
    }
    dfs(0, 0)
    return total
}
func main() { fmt.Println(subsetXORSum([]int{1,3}), subsetXORSum([]int{5,1,6})) }
