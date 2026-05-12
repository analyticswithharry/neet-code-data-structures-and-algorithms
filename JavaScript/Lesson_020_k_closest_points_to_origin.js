// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 020 -- K Closest Points to Origin
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 10
// =============================================================
//
// QUESTION:
//   Given an array of points where points[i] = [xi, yi] and an integer k,
//   return the k closest points to the origin (0, 0). Distance is Euclidean.
//
//   Example:
//     Input : points = [[1,3],[-2,2]], k = 1
//     Output: [[-2,2]]
// =============================================================

var kClosest = function(points, k) {
    return points.slice().sort((a,b) => (a[0]**2+a[1]**2) - (b[0]**2+b[1]**2)).slice(0, k);
};
console.log(kClosest([[1,3],[-2,2]], 1));
console.log(kClosest([[3,3],[5,-1],[-2,4]], 2));
