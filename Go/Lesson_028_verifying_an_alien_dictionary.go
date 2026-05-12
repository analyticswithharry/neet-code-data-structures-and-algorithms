//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 028 -- Verifying An Alien Dictionary
// Category   : Graphs
// Difficulty : Easy
// Study Plan : Day 14
// =============================================================
//
// QUESTION:
//   In an alien language, surprisingly, they also use English lowercase
//   letters but possibly in a different order. Given a sequence of words
//   written in the alien language and the order of the alphabet, return true
//   iff the given words are sorted lexicographically in this alien language.
//
//   Example:
//     Input : words=["hello","leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"
//     Output: true
// =============================================================

package main
import "fmt"
func isAlienSorted(words []string, order string) bool {
    idx := [26]int{}; for i := 0; i < 26; i++ { idx[order[i]-'a'] = i }
    for w := 1; w < len(words); w++ {
        a, b := words[w-1], words[w]; broke := false
        n := len(a); if len(b) < n { n = len(b) }
        for i := 0; i < n; i++ {
            ia, ib := idx[a[i]-'a'], idx[b[i]-'a']
            if ia != ib { if ia > ib { return false }; broke = true; break }
        }
        if !broke && len(a) > len(b) { return false }
    }
    return true
}
func main() { fmt.Println(isAlienSorted([]string{"hello","leetcode"}, "hlabcdefgijkmnopqrstuvwxyz")) }
