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

var isAlienSorted = function(words, order) {
    const idx = {}; for (let i = 0; i < order.length; i++) idx[order[i]] = i;
    for (let w = 1; w < words.length; w++) {
        const a = words[w-1], b = words[w]; let ok = false;
        for (let i = 0; i < Math.min(a.length, b.length); i++) {
            if (idx[a[i]] !== idx[b[i]]) { if (idx[a[i]] > idx[b[i]]) return false; ok = true; break; }
        }
        if (!ok && a.length > b.length) return false;
    }
    return true;
};
console.log(isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"));
