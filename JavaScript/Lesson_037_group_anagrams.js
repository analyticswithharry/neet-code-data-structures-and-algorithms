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

var groupAnagrams = function(strs) {
    const m = new Map();
    for (const s of strs) {
        const k = s.split("").sort().join("");
        if (!m.has(k)) m.set(k, []);
        m.get(k).push(s);
    }
    return [...m.values()];
};
console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]));
