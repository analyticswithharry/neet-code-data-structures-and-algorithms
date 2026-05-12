//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 037 -- Group Anagrams
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 18
// =============================================================
//
// QUESTION:
//   Given an array of strings strs, group the anagrams together.
//
//   Example: ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"],["tan","nat"],["bat"]]
// =============================================================

package main
import ("fmt"; "sort"; "strings")
func groupAnagrams(strs []string) [][]string {
    m := map[string][]string{}
    for _,s := range strs {
        b := []byte(s); sort.Slice(b, func(i,j int) bool{return b[i]<b[j]})
        k := string(b); m[k] = append(m[k], s)
    }
    out := [][]string{}
    for _,v := range m { out = append(out, v) }
    _ = strings.Join
    return out
}
func main(){ fmt.Println(groupAnagrams([]string{"eat","tea","tan","ate","nat","bat"})) }
