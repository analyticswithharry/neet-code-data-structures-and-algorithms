//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 012 -- Design Add And Search Words Data Structure
// Category   : Tries
// Difficulty : Medium
// Study Plan : Day 6
// =============================================================
//
// QUESTION:
//   Design a data structure that supports:
//     addWord(word)
//     search(word)  - word may contain '.' which matches any single letter
//
//   Example:
//     d = WordDictionary(); d.addWord("bad"); d.addWord("dad"); d.addWord("mad")
//     d.search("pad") -> False
//     d.search("bad") -> True
//     d.search(".ad") -> True
//     d.search("b..") -> True
// =============================================================

package main

import "fmt"

type WordDictionary struct { ch map[byte]*WordDictionary; end bool }
func NewWD() *WordDictionary { return &WordDictionary{ch: map[byte]*WordDictionary{}} }
func (d *WordDictionary) AddWord(w string) {
    n := d
    for i := 0; i < len(w); i++ {
        c := w[i]
        if _, ok := n.ch[c]; !ok { n.ch[c] = NewWD() }
        n = n.ch[c]
    }
    n.end = true
}
func (d *WordDictionary) Search(w string) bool { return dfs(0, w, d) }
func dfs(i int, w string, n *WordDictionary) bool {
    if i == len(w) { return n.end }
    c := w[i]
    if c == '.' {
        for _, x := range n.ch { if dfs(i+1, w, x) { return true } }
        return false
    }
    nx, ok := n.ch[c]
    return ok && dfs(i+1, w, nx)
}

func main() {
    d := NewWD()
    for _, w := range []string{"bad","dad","mad"} { d.AddWord(w) }
    fmt.Println(d.Search("pad"), d.Search("bad"), d.Search(".ad"), d.Search("b.."))
}
