// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 057 -- Find Minimum in Rotated Sorted Array
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 28
// =============================================================
//
// QUESTION:
//   Given a rotated sorted array of unique elements, return its minimum.
//
//   Example: [3,4,5,1,2] -> 1
// =============================================================

var findMin = function(nums) {
    let l = 0, r = nums.length - 1;
    while (l < r) {
        const mid = (l+r) >> 1;
        if (nums[mid] > nums[r]) l = mid+1; else r = mid;
    }
    return nums[l];
};
console.log(findMin([3,4,5,1,2]), findMin([4,5,6,7,0,1,2]));
