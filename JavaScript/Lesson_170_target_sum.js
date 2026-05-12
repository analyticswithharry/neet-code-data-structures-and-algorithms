// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 170 -- Target Sum
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 85
// =============================================================
//
// QUESTION:
//   Assign + or - to each number so the sum equals target. Return number of ways.
// =============================================================
function findTargetSumWays(nums,target){let dp=new Map([[0,1]]);for(const n of nums){const nd=new Map();for(const [s,c] of dp){nd.set(s+n,(nd.get(s+n)||0)+c);nd.set(s-n,(nd.get(s-n)||0)+c);}dp=nd;}return dp.get(target)||0;}
console.log(findTargetSumWays([1,1,1,1,1],3));
