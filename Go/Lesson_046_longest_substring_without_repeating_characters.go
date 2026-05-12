//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 046 -- Longest Substring Without Repeating Characters
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 23
// =============================================================
//
// QUESTION:
//   Given a string, find the length of the longest substring without
//   repeating characters.
//
//   Example: "abcabcbb" -> 3
// =============================================================

package main
import "fmt"
func lengthOfLongestSubstring(s string) int {
    seen := map[byte]int{}; l, best := 0, 0
    for r:=0;r<len(s);r++ {
        if v,ok := seen[s[r]]; ok && v >= l { l = v + 1 }
        seen[s[r]] = r
        if r-l+1 > best { best = r-l+1 }
    }
    return best
}
func main(){ fmt.Println(lengthOfLongestSubstring("abcabcbb"), lengthOfLongestSubstring("bbbbb")) }
