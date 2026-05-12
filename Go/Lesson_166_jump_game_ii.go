//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 166 -- Jump Game II
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 83
// =============================================================
//
// QUESTION:
//   Return the minimum number of jumps to reach the last index. Assume reachable.
// =============================================================
package main
import "fmt"
func jump(a []int) int { j,cur,far:=0,0,0; for i:=0;i<len(a)-1;i++ { if i+a[i]>far { far=i+a[i] }; if i==cur { j++; cur=far } }; return j }
func main(){ fmt.Println(jump([]int{2,3,1,1,4})); fmt.Println(jump([]int{2,3,0,1,4})) }
