//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 200 -- Edit Distance
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 100
// =============================================================
//
// QUESTION:
//   Min number of insert/delete/replace ops to convert s1 to s2.
// =============================================================
package main
import "fmt"
func minDistance(a,b string) int { m,n:=len(a),len(b); dp:=make([][]int,m+1); for i:=range dp { dp[i]=make([]int,n+1); dp[i][0]=i }; for j:=0;j<=n;j++ { dp[0][j]=j }; for i:=1;i<=m;i++ { for j:=1;j<=n;j++ { if a[i-1]==b[j-1] { dp[i][j]=dp[i-1][j-1] } else { mn:=dp[i-1][j]; if dp[i][j-1]<mn { mn=dp[i][j-1] }; if dp[i-1][j-1]<mn { mn=dp[i-1][j-1] }; dp[i][j]=1+mn } } }; return dp[m][n] }
func main(){ fmt.Println(minDistance("horse","ros")); fmt.Println(minDistance("intention","execution")) }
