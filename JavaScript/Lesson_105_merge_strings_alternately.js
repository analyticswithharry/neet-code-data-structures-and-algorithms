// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 105 -- Merge Strings Alternately
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 53
// =============================================================
//
// QUESTION:
//   Given two strings, merge them by adding letters in alternating order, starting with word1. If one is longer, append the rest.
// =============================================================

var mergeAlternately = function(a, b){
  let res=""; let i=0;
  while (i<a.length || i<b.length){ if (i<a.length) res+=a[i]; if (i<b.length) res+=b[i]; i++; }
  return res;
};
console.log(mergeAlternately("abc","pqr"), mergeAlternately("ab","pqrs"));
