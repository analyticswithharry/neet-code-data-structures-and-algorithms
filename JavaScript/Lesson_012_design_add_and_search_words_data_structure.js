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

class WordDictionary {
    constructor() { this.ch = {}; this.end = false; }
    addWord(w) { let n = this; for (const c of w) { if (!n.ch[c]) n.ch[c] = new WordDictionary(); n = n.ch[c]; } n.end = true; }
    search(w) {
        const dfs = (i, n) => {
            if (i === w.length) return n.end;
            const c = w[i];
            if (c === '.') return Object.values(n.ch).some(x => dfs(i+1, x));
            return n.ch[c] !== undefined && dfs(i+1, n.ch[c]);
        };
        return dfs(0, this);
    }
}
const d = new WordDictionary();
["bad","dad","mad"].forEach(w => d.addWord(w));
console.log(d.search("pad"), d.search("bad"), d.search(".ad"), d.search("b.."));
