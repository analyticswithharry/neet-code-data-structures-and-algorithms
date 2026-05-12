// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 026 -- Network Delay Time
// Category   : Advanced Graphs
// Difficulty : Medium
// Study Plan : Day 13
// =============================================================
//
// QUESTION:
//   You are given a network of n nodes labeled from 1 to n. times[i] =
//   [u,v,w] means a signal takes w time from u to v. Starting from node k,
//   return the time it takes for all nodes to receive the signal. If
//   impossible, return -1.
//
//   Example:
//     Input : times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
//     Output: 2
// =============================================================

var networkDelayTime = function(times, n, k) {
    const g = new Map();
    for (const [u,v,w] of times) { if (!g.has(u)) g.set(u, []); g.get(u).push([v,w]); }
    const dist = new Map(); const pq = [[0,k]];
    while (pq.length) {
        pq.sort((a,b) => b[0]-a[0]);
        const [d, u] = pq.pop();
        if (dist.has(u)) continue;
        dist.set(u, d);
        for (const [v,w] of (g.get(u) || [])) if (!dist.has(v)) pq.push([d+w, v]);
    }
    if (dist.size < n) return -1;
    return Math.max(...dist.values());
};
console.log(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2));
