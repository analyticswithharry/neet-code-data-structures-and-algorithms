// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 184 -- Missing Number
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 92
// =============================================================
//
// QUESTION:
//   Array contains n distinct numbers from [0,n]. Return the missing one.
// =============================================================
function missing(a){let x=a.length;for(let i=0;i<a.length;i++){x^=i^a[i];}return x;}
console.log(missing([3,0,1]));console.log(missing([9,6,4,2,3,5,7,0,1]));
