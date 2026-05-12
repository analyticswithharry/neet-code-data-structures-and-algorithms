// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 178 -- Longest Increasing Subsequence
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 89
// =============================================================
//
// QUESTION:
//   Length of the longest strictly-increasing subsequence.
// =============================================================
function LIS(a){const t=[];for(const x of a){let lo=0,hi=t.length;while(lo<hi){const m=(lo+hi)>>1;if(t[m]<x)lo=m+1;else hi=m;}t[lo]=x;}return t.length;}
console.log(LIS([10,9,2,5,3,7,101,18]));console.log(LIS([0,1,0,3,2,3]));
