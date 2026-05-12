// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 058 -- Search in Rotated Sorted Array
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 29
// =============================================================
//
// QUESTION:
//   Search target in a rotated sorted array of unique values.
//   Return its index, or -1 if not found.
//
//   Example: nums=[4,5,6,7,0,1,2], target=0 -> 4
// =============================================================

var search = function(nums, target) {
    let l = 0, r = nums.length - 1;
    while (l <= r) {
        const mid = (l+r) >> 1;
        if (nums[mid] === target) return mid;
        if (nums[l] <= nums[mid]) {
            if (nums[l] <= target && target < nums[mid]) r = mid-1;
            else l = mid+1;
        } else {
            if (nums[mid] < target && target <= nums[r]) l = mid+1;
            else r = mid-1;
        }
    }
    return -1;
};
console.log(search([4,5,6,7,0,1,2], 0), search([4,5,6,7,0,1,2], 3));
