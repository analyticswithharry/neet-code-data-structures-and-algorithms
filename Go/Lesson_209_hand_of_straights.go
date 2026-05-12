//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 209 -- Hand of Straights
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 105
// =============================================================
//
// QUESTION:
//   Can hand be rearranged into groups of size W of consecutive cards?
// =============================================================
package main
import ("fmt"; "sort")
func isNStraightHand(h []int,W int) bool { if len(h)%W!=0 { return false }; c:=map[int]int{}; for _,x:=range h { c[x]++ }; keys:=[]int{}; for k:=range c { keys=append(keys,k) }; sort.Ints(keys); for _,x:=range keys { cnt:=c[x]; if cnt>0 { for k:=0;k<W;k++ { if c[x+k]<cnt { return false }; c[x+k]-=cnt } } }; return true }
func main(){ fmt.Println(isNStraightHand([]int{1,2,3,6,2,3,4,7,8},3)); fmt.Println(isNStraightHand([]int{1,2,3,4,5},4)) }
