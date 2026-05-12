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

class Trie {
    constructor() { this.ch = {}; this.end = false; }
    insert(w) { let n = this; for (const c of w) { if (!n.ch[c]) n.ch[c] = new Trie(); n = n.ch[c]; } n.end = true; }
    _walk(w) { let n = this; for (const c of w) { if (!n.ch[c]) return null; n = n.ch[c]; } return n; }
    search(w) { const n = this._walk(w); return !!n && n.end; }
    startsWith(p) { return this._walk(p) !== null; }
}

const t = new Trie(); t.insert("apple");
console.log(t.search("apple"), t.search("app"), t.startsWith("app"));
t.insert("app"); console.log(t.search("app"));
