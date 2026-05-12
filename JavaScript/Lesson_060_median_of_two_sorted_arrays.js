// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 060 -- Median of Two Sorted Arrays
// Category   : Binary Search
// Difficulty : Hard
// Study Plan : Day 30
// =============================================================
//
// QUESTION:
//   Given two sorted arrays nums1 and nums2, return the median of the
//   combined sorted array. Run in O(log(min(m,n))).
//
//   Example: [1,3], [2] -> 2.0
// =============================================================

var findMedianSortedArrays = function(a, b) {
    if (a.length > b.length) [a, b] = [b, a];
    const m = a.length, n = b.length, half = ((m+n+1) >> 1);
    let lo = 0, hi = m;
    while (lo <= hi) {
        const i = (lo+hi) >> 1, j = half - i;
        const la = i>0 ? a[i-1] : -Infinity;
        const ra = i<m ? a[i]   :  Infinity;
        const lb = j>0 ? b[j-1] : -Infinity;
        const rb = j<n ? b[j]   :  Infinity;
        if (la <= rb && lb <= ra) {
            if ((m+n) % 2) return Math.max(la, lb);
            return (Math.max(la, lb) + Math.min(ra, rb)) / 2;
        } else if (la > rb) hi = i-1;
        else lo = i+1;
    }
    return 0;
};
console.log(findMedianSortedArrays([1,3], [2]));
console.log(findMedianSortedArrays([1,2], [3,4]));
