// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 110 -- Longest Repeating Character Replacement
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 55
// =============================================================
//
// QUESTION:
//   Given a string s and integer k, you may change up to k characters. Return length of longest substring with all same characters.
// =============================================================

var characterReplacement = function(s, k){
  const cnt={}; let l=0, mx=0, best=0;
  for (let r=0;r<s.length;r++){
    const c=s[r]; cnt[c]=(cnt[c]||0)+1; mx=Math.max(mx, cnt[c]);
    if (r-l+1 - mx > k){ cnt[s[l]]--; l++; }
    best = Math.max(best, r-l+1);
  }
  return best;
};
console.log(characterReplacement("ABAB", 2), characterReplacement("AABABBA", 1));
