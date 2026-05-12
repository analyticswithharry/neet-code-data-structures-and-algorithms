//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 105 -- Merge Strings Alternately
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 53
// =============================================================
//
// QUESTION:
//   Given two strings, merge them by adding letters in alternating order, starting with word1. If one is longer, append the rest.
// =============================================================

package main
import "fmt"
func mergeAlternately(a, b string) string {
    r := []byte{}; i := 0
    for i < len(a) || i < len(b) {
        if i < len(a) { r = append(r, a[i]) }
        if i < len(b) { r = append(r, b[i]) }
        i++
    }
    return string(r)
}
func main(){ fmt.Println(mergeAlternately("abc","pqr"), mergeAlternately("ab","pqrs")) }
