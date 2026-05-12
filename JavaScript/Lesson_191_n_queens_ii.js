// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 191 -- N Queens II
// Category   : Backtracking
// Difficulty : Hard
// Study Plan : Day 96
// =============================================================
//
// QUESTION:
//   Return number of distinct solutions for n-queens.
// =============================================================
function totalNQueens(n){let cnt=0;const c=new Set(),d1=new Set(),d2=new Set();function bt(r){if(r===n){cnt++;return;}for(let i=0;i<n;i++){if(c.has(i)||d1.has(r-i)||d2.has(r+i))continue;c.add(i);d1.add(r-i);d2.add(r+i);bt(r+1);c.delete(i);d1.delete(r-i);d2.delete(r+i);}}bt(0);return cnt;}
console.log(totalNQueens(4));console.log(totalNQueens(8));
