// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 046 -- Longest Substring Without Repeating Characters
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 23
// =============================================================
//
// QUESTION:
//   Given a string, find the length of the longest substring without
//   repeating characters.
//
//   Example: "abcabcbb" -> 3
// =============================================================

var lengthOfLongestSubstring = function(s) {
    const seen = {}; let l = 0, best = 0;
    for (let r=0;r<s.length;r++) {
        const c = s[r];
        if (seen[c] !== undefined && seen[c] >= l) l = seen[c] + 1;
        seen[c] = r;
        best = Math.max(best, r - l + 1);
    }
    return best;
};
console.log(lengthOfLongestSubstring("abcabcbb"), lengthOfLongestSubstring("bbbbb"));
