// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 172 -- N Queens
// Category   : Backtracking
// Difficulty : Hard
// Study Plan : Day 86
// =============================================================
//
// QUESTION:
//   Place n queens on n×n board so none attack each other; return the count of distinct solutions.
// =============================================================
function totalNQueens(n){let cnt=0;const cols=new Set(),d1=new Set(),d2=new Set();function bt(r){if(r===n){cnt++;return;}for(let c=0;c<n;c++){if(cols.has(c)||d1.has(r-c)||d2.has(r+c))continue;cols.add(c);d1.add(r-c);d2.add(r+c);bt(r+1);cols.delete(c);d1.delete(r-c);d2.delete(r+c);}}bt(0);return cnt;}
console.log(totalNQueens(4));console.log(totalNQueens(6));
