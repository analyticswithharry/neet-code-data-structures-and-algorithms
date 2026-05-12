//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 011 -- Implement Trie Prefix Tree
// Category   : Tries
// Difficulty : Medium
// Study Plan : Day 6
// =============================================================
//
// QUESTION:
//   Implement the Trie class with:
//     insert(word)        - inserts the word
//     search(word)        - returns true if word is in trie
//     startsWith(prefix)  - returns true if any word starts with prefix
//
//   Example:
//     trie = Trie()
//     trie.insert("apple")
//     trie.search("apple")   -> True
//     trie.search("app")     -> False
//     trie.startsWith("app") -> True
//     trie.insert("app")
//     trie.search("app")     -> True
// =============================================================

package main

import "fmt"

type Trie struct { ch map[rune]*Trie; end bool }
func NewTrie() *Trie { return &Trie{ch: map[rune]*Trie{}} }
func (t *Trie) Insert(w string) {
    n := t
    for _, c := range w {
        if _, ok := n.ch[c]; !ok { n.ch[c] = NewTrie() }
        n = n.ch[c]
    }
    n.end = true
}
func (t *Trie) walk(w string) *Trie {
    n := t
    for _, c := range w {
        nx, ok := n.ch[c]; if !ok { return nil }; n = nx
    }
    return n
}
func (t *Trie) Search(w string) bool { n := t.walk(w); return n != nil && n.end }
func (t *Trie) StartsWith(p string) bool { return t.walk(p) != nil }

func main() {
    t := NewTrie(); t.Insert("apple")
    fmt.Println(t.Search("apple"), t.Search("app"), t.StartsWith("app"))
    t.Insert("app"); fmt.Println(t.Search("app"))
}
