//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 086 -- Longest Substring Without Repeating Characters
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 43
// =============================================================
//
// QUESTION:
//   Given a string s, find the length of the longest substring without repeating characters.
//   Example: 'abcabcbb' -> 3 ('abc'); 'bbbbb' -> 1; 'pwwkew' -> 3.
// =============================================================

package main
import "fmt"
func lengthOfLongestSubstring(s string) int {
    m := map[byte]int{}; l, best := 0, 0
    for r := 0; r < len(s); r++ {
        c := s[r]
        if v, ok := m[c]; ok && v >= l { l = v + 1 }
        m[c] = r
        if r-l+1 > best { best = r-l+1 }
    }
    return best
}
func main(){ fmt.Println(lengthOfLongestSubstring("abcabcbb"), lengthOfLongestSubstring("pwwkew")) }
