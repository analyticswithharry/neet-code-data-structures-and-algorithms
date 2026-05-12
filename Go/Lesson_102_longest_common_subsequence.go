//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 102 -- Longest Common Subsequence
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 51
// =============================================================
//
// QUESTION:
//   Given two strings text1 and text2, return the length of their longest common subsequence.
// =============================================================

package main
import "fmt"
func longestCommonSubsequence(a, b string) int {
    m, n := len(a), len(b)
    dp := make([][]int, m+1); for i := range dp { dp[i] = make([]int, n+1) }
    for i := 0; i < m; i++ { for j := 0; j < n; j++ {
        if a[i]==b[j] { dp[i+1][j+1] = dp[i][j]+1
        } else { x, y := dp[i][j+1], dp[i+1][j]; if x>y { dp[i+1][j+1]=x } else { dp[i+1][j+1]=y } }
    }}
    return dp[m][n]
}
func main(){ fmt.Println(longestCommonSubsequence("abcde","ace")) }
