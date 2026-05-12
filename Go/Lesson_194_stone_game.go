//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 194 -- Stone Game
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 97
// =============================================================
//
// QUESTION:
//   Two players take stones from either end. Both play optimally. Return true if Alice wins.
// =============================================================
package main
import "fmt"
func stoneGame(p []int) bool { n:=len(p); dp:=make([][]int,n); for i:=range dp { dp[i]=make([]int,n); dp[i][i]=p[i] }; for L:=2;L<=n;L++ { for i:=0;i<=n-L;i++ { j:=i+L-1; a:=p[i]-dp[i+1][j]; b:=p[j]-dp[i][j-1]; if a>b { dp[i][j]=a } else { dp[i][j]=b } } }; return dp[0][n-1]>0 }
func main(){ fmt.Println(stoneGame([]int{5,3,4,5})) }
