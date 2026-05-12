// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 040 -- Longest Consecutive Sequence
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 20
// =============================================================
//
// QUESTION:
//   Given an unsorted array, return the length of the longest consecutive
//   elements sequence in O(n).
//
//   Example: [100,4,200,1,3,2] -> 4 (sequence 1,2,3,4)
// =============================================================

var longestConsecutive = function(nums) {
    const s = new Set(nums); let best = 0;
    for (const n of s) {
        if (!s.has(n-1)) {
            let cur = n, len = 1;
            while (s.has(cur+1)) { cur++; len++; }
            best = Math.max(best, len);
        }
    }
    return best;
};
console.log(longestConsecutive([100,4,200,1,3,2]));
