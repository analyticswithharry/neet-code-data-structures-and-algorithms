// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 036 -- Valid Anagram
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 18
// =============================================================
//
// QUESTION:
//   Given two strings s and t, return true if t is an anagram of s.
//
//   Example: s = "anagram", t = "nagaram" -> true
// =============================================================

var isAnagram = function(s, t) {
    if (s.length !== t.length) return false;
    const d = {};
    for (const c of s) d[c] = (d[c]||0)+1;
    for (const c of t) { if (!d[c]) return false; d[c]--; }
    return true;
};
console.log(isAnagram("anagram","nagaram"), isAnagram("rat","car"));
