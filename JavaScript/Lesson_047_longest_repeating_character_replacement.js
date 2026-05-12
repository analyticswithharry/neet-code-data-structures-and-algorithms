// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 047 -- Longest Repeating Character Replacement
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 23
// =============================================================
//
// QUESTION:
//   Given a string s and integer k, you can change at most k characters.
//   Return length of the longest substring with all same characters.
//
//   Example: s="AABABBA", k=1 -> 4
// =============================================================

var characterReplacement = function(s, k) {
    const cnt = {}; let l=0, best=0, mf=0;
    for (let r=0;r<s.length;r++) {
        cnt[s[r]] = (cnt[s[r]]||0)+1;
        mf = Math.max(mf, cnt[s[r]]);
        if (r - l + 1 - mf > k) { cnt[s[l]]--; l++; }
        best = Math.max(best, r - l + 1);
    }
    return best;
};
console.log(characterReplacement("AABABBA", 1));
