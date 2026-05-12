//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 093 -- Alien Dictionary
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 47
// =============================================================
//
// QUESTION:
//   Given a sorted list of words from an alien language, derive the order of letters. Return any valid order or '' if impossible.
// =============================================================

package main
import "fmt"
func alienOrder(words []string) string {
    g := map[byte]map[byte]bool{}; ind := map[byte]int{}
    for _, w := range words { for i := 0; i < len(w); i++ {
        if _, ok := g[w[i]]; !ok { g[w[i]] = map[byte]bool{} }
        if _, ok := ind[w[i]]; !ok { ind[w[i]] = 0 }
    }}
    for i := 0; i < len(words)-1; i++ {
        a, b := words[i], words[i+1]; found := false
        m := len(a); if len(b) < m { m = len(b) }
        for j := 0; j < m; j++ {
            if a[j] != b[j] { if !g[a[j]][b[j]] { g[a[j]][b[j]] = true; ind[b[j]]++ }; found = true; break }
        }
        if !found && len(a) > len(b) { return "" }
    }
    q := []byte{}; for c, v := range ind { if v == 0 { q = append(q, c) } }
    res := []byte{}
    for len(q) > 0 {
        c := q[0]; q = q[1:]; res = append(res, c)
        for nx := range g[c] { ind[nx]--; if ind[nx] == 0 { q = append(q, nx) } }
    }
    if len(res) != len(ind) { return "" }
    return string(res)
}
func main(){ fmt.Println(alienOrder([]string{"wrt","wrf","er","ett","rftt"})) }
