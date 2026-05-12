// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 044 -- Trapping Rain Water
// Category   : Two Pointers
// Difficulty : Hard
// Study Plan : Day 22
// =============================================================
//
// QUESTION:
//   Given heights, compute how much water can be trapped after raining.
//
//   Example: [0,1,0,2,1,0,1,3,2,1,2,1] -> 6
// =============================================================

var trap = function(h) {
    let l=0, r=h.length-1, lm=0, rm=0, ans=0;
    while (l<r) {
        if (h[l]<h[r]) { lm=Math.max(lm,h[l]); ans+=lm-h[l]; l++; }
        else { rm=Math.max(rm,h[r]); ans+=rm-h[r]; r--; }
    }
    return ans;
};
console.log(trap([0,1,0,2,1,0,1,3,2,1,2,1]));
