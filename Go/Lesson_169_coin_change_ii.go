//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 169 -- Coin Change II
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 85
// =============================================================
//
// QUESTION:
//   Number of distinct combinations of coins (unlimited) summing to amount.
// =============================================================
package main
import "fmt"
func change(amt int,coins []int) int { dp:=make([]int,amt+1); dp[0]=1; for _,c:=range coins { for a:=c; a<=amt; a++ { dp[a]+=dp[a-c] } }; return dp[amt] }
func main(){ fmt.Println(change(5,[]int{1,2,5})); fmt.Println(change(3,[]int{2})) }
