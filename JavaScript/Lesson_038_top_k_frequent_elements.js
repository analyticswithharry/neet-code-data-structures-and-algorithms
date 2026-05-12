// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 038 -- Top K Frequent Elements
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 19
// =============================================================
//
// QUESTION:
//   Given an integer array nums and integer k, return the k most frequent elements.
//
//   Example: nums = [1,1,1,2,2,3], k = 2 -> [1,2]
// =============================================================

var topKFrequent = function(nums, k) {
    const m = new Map();
    for (const n of nums) m.set(n,(m.get(n)||0)+1);
    return [...m.entries()].sort((a,b)=>b[1]-a[1]).slice(0,k).map(e=>e[0]);
};
console.log(topKFrequent([1,1,1,2,2,3], 2));
