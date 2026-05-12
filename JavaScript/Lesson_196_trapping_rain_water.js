// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 196 -- Trapping Rain Water
// Category   : Two Pointers
// Difficulty : Hard
// Study Plan : Day 98
// =============================================================
//
// QUESTION:
//   Compute total water trapped between bars given heights.
// =============================================================
function trap(h){let l=0,r=h.length-1,lm=0,rm=0,res=0;while(l<r){if(h[l]<h[r]){if(h[l]>=lm)lm=h[l];else res+=lm-h[l];l++;}else{if(h[r]>=rm)rm=h[r];else res+=rm-h[r];r--;}}return res;}
console.log(trap([0,1,0,2,1,0,1,3,2,1,2,1]));
