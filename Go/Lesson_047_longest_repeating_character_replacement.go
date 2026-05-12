//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 047 -- Longest Repeating Character Replacement
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 23
// =============================================================
//
// QUESTION:
//   Given a string s and integer k, you can change at most k characters.
//   Return length of the longest substring with all same characters.
//
//   Example: s="AABABBA", k=1 -> 4
// =============================================================

package main
import "fmt"
func characterReplacement(s string, k int) int {
    var cnt [26]int; l, best, mf := 0, 0, 0
    max := func(a,b int) int { if a>b {return a}; return b }
    for r:=0; r<len(s); r++ {
        cnt[s[r]-'A']++; mf = max(mf, cnt[s[r]-'A'])
        if r - l + 1 - mf > k { cnt[s[l]-'A']--; l++ }
        best = max(best, r - l + 1)
    }
    return best
}
func main(){ fmt.Println(characterReplacement("AABABBA", 1)) }
