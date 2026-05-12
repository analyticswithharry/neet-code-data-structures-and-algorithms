// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 106 -- Rotate Array
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 53
// =============================================================
//
// QUESTION:
//   Rotate the array to the right by k steps in-place.
// =============================================================

var rotate = function(nums, k){
  const n=nums.length; k = k % n;
  const rev = (l, r)=>{ while(l<r){ [nums[l], nums[r]]=[nums[r], nums[l]]; l++; r--; } };
  rev(0, n-1); rev(0, k-1); rev(k, n-1);
};
const a=[1,2,3,4,5,6,7]; rotate(a, 3); console.log(JSON.stringify(a));
