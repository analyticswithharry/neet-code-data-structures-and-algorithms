//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 167 -- Coin Change
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 84
// =============================================================
//
// QUESTION:
//   Fewest coins needed to make up amount; coins are unlimited. Return -1 if impossible.
// =============================================================
package main
import "fmt"
func coinChange(coins []int,amt int) int { INF:=1<<30; dp:=make([]int,amt+1); for i:=range dp { dp[i]=INF }; dp[0]=0; for a:=1;a<=amt;a++ { for _,c:=range coins { if c<=a && dp[a-c]+1<dp[a] { dp[a]=dp[a-c]+1 } } }; if dp[amt]>=INF { return -1 }; return dp[amt] }
func main(){ fmt.Println(coinChange([]int{1,2,5},11)); fmt.Println(coinChange([]int{2},3)) }
