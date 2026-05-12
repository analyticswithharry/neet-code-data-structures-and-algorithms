// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 039 -- Product of Array Except Self
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 19
// =============================================================
//
// QUESTION:
//   Given nums, return an array where answer[i] is the product of all elements
//   except nums[i]. Must run in O(n) without division.
//
//   Example: [1,2,3,4] -> [24,12,8,6]
// =============================================================

var productExceptSelf = function(nums) {
    const n = nums.length, r = new Array(n).fill(1);
    let left = 1;
    for (let i=0;i<n;i++){ r[i]=left; left*=nums[i]; }
    let right = 1;
    for (let i=n-1;i>=0;i--){ r[i]*=right; right*=nums[i]; }
    return r;
};
console.log(productExceptSelf([1,2,3,4]));
