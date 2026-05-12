//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 023 -- Extra Characters in a String
// Category   : Tries
// Difficulty : Medium
// Study Plan : Day 12
// =============================================================
//
// QUESTION:
//   Given a string s and a dictionary of words, break s into one or more
//   non-overlapping substrings such that each substring is in dictionary.
//   There may be characters in s that are not in any of the substrings.
//   Return the minimum number of extra characters left over.
//
//   Example:
//     Input : s = "leetscode", dict = ["leet","code","leetcode"]
//     Output: 1   (the 's' is extra)
// =============================================================

package main
import "fmt"
func minExtraChar(s string, dictionary []string) int {
    words := map[string]bool{}; for _, w := range dictionary { words[w] = true }
    n := len(s); dp := make([]int, n+1)
    for i := 1; i <= n; i++ {
        dp[i] = dp[i-1] + 1
        for j := 0; j < i; j++ {
            if words[s[j:i]] && dp[j] < dp[i] { dp[i] = dp[j] }
        }
    }
    return dp[n]
}
func main() { fmt.Println(minExtraChar("leetscode", []string{"leet","code","leetcode"})) }
