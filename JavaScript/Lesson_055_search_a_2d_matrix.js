// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 055 -- Search a 2D Matrix
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 27
// =============================================================
//
// QUESTION:
//   Given an m x n matrix sorted row-wise (and each row's first > prev row's last),
//   search for target.
//
//   Example: [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3 -> true
// =============================================================

var searchMatrix = function(m, target) {
    if (!m.length || !m[0].length) return false;
    const rows = m.length, cols = m[0].length;
    let l = 0, r = rows*cols - 1;
    while (l <= r) {
        const mid = (l+r) >> 1;
        const v = m[Math.floor(mid/cols)][mid%cols];
        if (v === target) return true;
        if (v < target) l = mid+1; else r = mid-1;
    }
    return false;
};
console.log(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3));
console.log(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13));
