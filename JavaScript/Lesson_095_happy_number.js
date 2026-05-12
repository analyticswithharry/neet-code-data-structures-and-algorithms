// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 095 -- Happy Number
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 48
// =============================================================
//
// QUESTION:
//   A number is happy if repeatedly summing the squares of its digits eventually equals 1. Return true if n is happy.
// =============================================================

var isHappy = function(n){
  const seen=new Set();
  while (n!==1 && !seen.has(n)){
    seen.add(n);
    let s=0; while(n>0){ const d=n%10; s+=d*d; n=Math.floor(n/10); } n=s;
  }
  return n===1;
};
console.log(isHappy(19), isHappy(2));
