//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 048 -- Permutation in String
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 24
// =============================================================
//
// QUESTION:
//   Given s1 and s2, return true if s2 contains a permutation of s1.
//
//   Example: s1="ab", s2="eidbaooo" -> true
// =============================================================

package main
import "fmt"
func checkInclusion(s1, s2 string) bool {
    if len(s1) > len(s2) { return false }
    var a, b [26]int
    for i:=0;i<len(s1);i++ { a[s1[i]-'a']++; b[s2[i]-'a']++ }
    if a==b { return true }
    for i:=len(s1); i<len(s2); i++ {
        b[s2[i]-'a']++; b[s2[i-len(s1)]-'a']--
        if a==b { return true }
    }
    return false
}
func main(){ fmt.Println(checkInclusion("ab","eidbaooo"), checkInclusion("ab","eidboaoo")) }
