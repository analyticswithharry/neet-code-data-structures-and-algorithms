// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 086 -- Longest Substring Without Repeating Characters
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 43
// =============================================================
//
// QUESTION:
//   Given a string s, find the length of the longest substring without repeating characters.
//   Example: 'abcabcbb' -> 3 ('abc'); 'bbbbb' -> 1; 'pwwkew' -> 3.
// =============================================================

var lengthOfLongestSubstring = function(s){
  const m = new Map(); let l=0, best=0;
  for (let r=0;r<s.length;r++){
    const c=s[r];
    if (m.has(c) && m.get(c)>=l) l = m.get(c)+1;
    m.set(c,r); best = Math.max(best, r-l+1);
  } return best;
};
console.log(lengthOfLongestSubstring("abcabcbb"), lengthOfLongestSubstring("pwwkew"));
