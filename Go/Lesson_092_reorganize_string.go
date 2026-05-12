//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 092 -- Reorganize String
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 46
// =============================================================
//
// QUESTION:
//   Given a string s, rearrange so no two adjacent chars are equal. Return the rearranged string, or '' if impossible.
// =============================================================

package main
import "fmt"
func reorganizeString(s string) string {
    c := [26]int{}; for i := range s { c[s[i]-'a']++ }
    n := len(s); mx, idx := 0, 0
    for i := 0; i < 26; i++ { if c[i] > mx { mx, idx = c[i], i } }
    if mx > (n+1)/2 { return "" }
    res := make([]byte, n); i := 0
    for c[idx] > 0 { res[i] = byte('a'+idx); i += 2; c[idx]-- }
    for k := 0; k < 26; k++ {
        for c[k] > 0 { if i >= n { i = 1 }; res[i] = byte('a'+k); i += 2; c[k]-- }
    }
    return string(res)
}
func main(){ fmt.Println(reorganizeString("aab"), "["+reorganizeString("aaab")+"]") }
