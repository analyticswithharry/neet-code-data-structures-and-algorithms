//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 036 -- Valid Anagram
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 18
// =============================================================
//
// QUESTION:
//   Given two strings s and t, return true if t is an anagram of s.
//
//   Example: s = "anagram", t = "nagaram" -> true
// =============================================================

package main
import "fmt"
func isAnagram(s, t string) bool {
    if len(s)!=len(t){return false}
    var c [26]int
    for i:=0;i<len(s);i++ { c[s[i]-'a']++; c[t[i]-'a']-- }
    for _,x:=range c{ if x!=0 {return false} }
    return true
}
func main(){ fmt.Println(isAnagram("anagram","nagaram"), isAnagram("rat","car")) }
