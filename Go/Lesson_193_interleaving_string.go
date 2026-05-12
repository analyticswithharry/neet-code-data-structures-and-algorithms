//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 193 -- Interleaving String
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 97
// =============================================================
//
// QUESTION:
//   Determine whether s3 can be formed by interleaving s1 and s2.
// =============================================================
package main
import "fmt"
func isInterleave(a,b,c string) bool { if len(a)+len(b)!=len(c) { return false }; dp:=make([][]bool,len(a)+1); for i:=range dp { dp[i]=make([]bool,len(b)+1) }; dp[0][0]=true; for i:=0;i<=len(a);i++ { for j:=0;j<=len(b);j++ { if i>0 && a[i-1]==c[i+j-1] && dp[i-1][j] { dp[i][j]=true }; if j>0 && b[j-1]==c[i+j-1] && dp[i][j-1] { dp[i][j]=true } } }; return dp[len(a)][len(b)] }
func main(){ fmt.Println(isInterleave("aabcc","dbbca","aadbbcbcac")); fmt.Println(isInterleave("aabcc","dbbca","aadbbbaccc")) }
