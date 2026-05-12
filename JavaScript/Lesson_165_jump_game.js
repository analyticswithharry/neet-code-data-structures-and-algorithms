// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 165 -- Jump Game
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 83
// =============================================================
//
// QUESTION:
//   Each element is max jump length from that position. Return true iff you can reach the last index from index 0.
// =============================================================
function canJump(a){let r=0;for(let i=0;i<a.length;i++){if(i>r)return false;r=Math.max(r,i+a[i]);}return true;}
console.log(canJump([2,3,1,1,4]));console.log(canJump([3,2,1,0,4]));
