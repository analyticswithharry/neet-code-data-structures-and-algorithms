//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 110 -- Longest Repeating Character Replacement
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 55
// =============================================================
//
// QUESTION:
//   Given a string s and integer k, you may change up to k characters. Return length of longest substring with all same characters.
// =============================================================

package main
import "fmt"
func characterReplacement(s string, k int) int {
    cnt := [26]int{}; l, mx, best := 0, 0, 0
    for r := 0; r < len(s); r++ {
        cnt[s[r]-'A']++; if cnt[s[r]-'A']>mx { mx = cnt[s[r]-'A'] }
        if r-l+1 - mx > k { cnt[s[l]-'A']--; l++ }
        if r-l+1 > best { best = r-l+1 }
    }
    return best
}
func main(){ fmt.Println(characterReplacement("ABAB",2), characterReplacement("AABABBA",1)) }
