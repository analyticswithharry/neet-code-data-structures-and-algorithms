// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 097 -- Majority Element
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 49
// =============================================================
//
// QUESTION:
//   Given an array of size n, return the element that appears more than n/2 times.
// =============================================================

var majorityElement = function(nums){
  let cand=0, cnt=0;
  for (const n of nums){ if (cnt===0) cand=n; cnt += n===cand?1:-1; }
  return cand;
};
console.log(majorityElement([3,2,3]), majorityElement([2,2,1,1,1,2,2]));
