// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 052 -- Daily Temperatures
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 26
// =============================================================
//
// QUESTION:
//   Given temperatures, for each day return the number of days until a
//   warmer temperature, or 0 if none.
//
//   Example: [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
// =============================================================

var dailyTemperatures = function(t) {
    const n = t.length, res = new Array(n).fill(0), st = [];
    for (let i=0;i<n;i++) {
        while (st.length && t[st[st.length-1]] < t[i]) {
            const j = st.pop(); res[j] = i - j;
        }
        st.push(i);
    }
    return res;
};
console.log(dailyTemperatures([73,74,75,71,69,72,76,73]));
