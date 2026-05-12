//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 171 -- Partition to K Equal Sum Subsets
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 86
// =============================================================
//
// QUESTION:
//   Determine if nums can be partitioned into k subsets with equal sum.
// =============================================================
package main
import ("fmt"; "sort")
var (T,K int; N,B []int)
func bt(i int) bool { if i==len(N) { return true }; for j:=0;j<K;j++ { if B[j]+N[i]<=T { B[j]+=N[i]; if bt(i+1) { return true }; B[j]-=N[i] }; if B[j]==0 { break } }; return false }
func canPartitionKSubsets(nums []int,k int) bool { s:=0; for _,v:=range nums { s+=v }; if s%k!=0 { return false }; T=s/k; sort.Sort(sort.Reverse(sort.IntSlice(nums))); if nums[0]>T { return false }; K=k; N=nums; B=make([]int,k); return bt(0) }
func main(){ fmt.Println(canPartitionKSubsets([]int{4,3,2,3,5,2,1},4)) }
