// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 033 -- Last Stone Weight
// Category   : Heap Priority Queue
// Difficulty : Easy
// Study Plan : Day 17
// =============================================================
//
// QUESTION:
//   You are given an array of stones. On each turn pick the two heaviest
//   stones x <= y. If x == y both are destroyed; if x != y, x is destroyed
//   and y becomes y - x. Return the weight of the last remaining stone (or 0).
//
//   Example:
//     Input : [2,7,4,1,8,1]   Output: 1
// =============================================================

var lastStoneWeight = function(stones) {
    const a = stones.slice();
    while (a.length > 1) {
        a.sort((x,y) => x-y);
        const y = a.pop(), x = a.pop();
        if (y !== x) a.push(y - x);
    }
    return a[0] ?? 0;
};
console.log(lastStoneWeight([2,7,4,1,8,1]));
