//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 088 -- Permutations II
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 44
// =============================================================
//
// QUESTION:
//   Given a collection nums of numbers that might contain duplicates, return all possible unique permutations.
//   Example: [1,1,2] -> [[1,1,2],[1,2,1],[2,1,1]].
// =============================================================

package main
import ( "fmt"; "sort" )
func permuteUnique(nums []int) [][]int {
    sort.Ints(nums); var res [][]int; used := make([]bool,len(nums)); cur := []int{}
    var bt func()
    bt = func(){
        if len(cur)==len(nums){ tmp:=make([]int,len(cur)); copy(tmp,cur); res=append(res,tmp); return }
        for i := 0; i < len(nums); i++ {
            if used[i] { continue }
            if i>0 && nums[i]==nums[i-1] && !used[i-1] { continue }
            used[i]=true; cur=append(cur,nums[i]); bt()
            cur=cur[:len(cur)-1]; used[i]=false
        }
    }
    bt(); return res
}
func main(){ fmt.Println(permuteUnique([]int{1,1,2})) }
