//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 202 -- Distinct Subsequences
// Category   : 2-D Dynamic Programming
// Difficulty : Hard
// Study Plan : Day 101
// =============================================================
//
// QUESTION:
//   Number of distinct subsequences of s equal to t.
// =============================================================
package main
import "fmt"
func numDistinct(s,t string) int { m,n:=len(s),len(t); dp:=make([][]int,m+1); for i:=range dp { dp[i]=make([]int,n+1); dp[i][0]=1 }; for i:=1;i<=m;i++ { for j:=1;j<=n;j++ { dp[i][j]=dp[i-1][j]; if s[i-1]==t[j-1] { dp[i][j]+=dp[i-1][j-1] } } }; return dp[m][n] }
func main(){ fmt.Println(numDistinct("rabbbit","rabbit")) }
