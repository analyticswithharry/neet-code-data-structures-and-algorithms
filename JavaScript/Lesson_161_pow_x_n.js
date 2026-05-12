// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 161 -- Pow x n
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 81
// =============================================================
//
// QUESTION:
//   Implement pow(x, n) — x raised to the n-th power.
// =============================================================
function myPow(x,n){if(n<0){x=1/x;n=-n;}let r=1.0;while(n){if(n&1)r*=x;x*=x;n=Math.floor(n/2);}return r;}
console.log(myPow(2,10));console.log(myPow(2,-2));
