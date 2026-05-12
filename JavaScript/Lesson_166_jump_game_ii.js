// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 166 -- Jump Game II
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 83
// =============================================================
//
// QUESTION:
//   Return the minimum number of jumps to reach the last index. Assume reachable.
// =============================================================
function jump(a){let j=0,cur=0,far=0;for(let i=0;i<a.length-1;i++){far=Math.max(far,i+a[i]);if(i===cur){j++;cur=far;}}return j;}
console.log(jump([2,3,1,1,4]));console.log(jump([2,3,0,1,4]));
