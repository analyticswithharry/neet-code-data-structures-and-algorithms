// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 054 -- Largest Rectangle in Histogram
// Category   : Stack
// Difficulty : Hard
// Study Plan : Day 27
// =============================================================
//
// QUESTION:
//   Given heights of bars, find the area of the largest rectangle.
//
//   Example: [2,1,5,6,2,3] -> 10
// =============================================================

var largestRectangleArea = function(h) {
    const st = []; let best = 0;
    const h2 = [...h, 0];
    for (let i=0;i<h2.length;i++) {
        let start = i;
        while (st.length && st[st.length-1][1] > h2[i]) {
            const [idx, ht] = st.pop();
            best = Math.max(best, ht*(i-idx));
            start = idx;
        }
        st.push([start, h2[i]]);
    }
    return best;
};
console.log(largestRectangleArea([2,1,5,6,2,3]));
