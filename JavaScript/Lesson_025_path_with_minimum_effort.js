// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 025 -- Path with Minimum Effort
// Category   : Advanced Graphs
// Difficulty : Medium
// Study Plan : Day 13
// =============================================================
//
// QUESTION:
//   Given an m x n grid of heights, find a path from top-left to
//   bottom-right that minimizes the maximum absolute difference in heights
//   between consecutive cells along the path.
//
//   Example:
//     Input : heights = [[1,2,2],[3,8,2],[5,3,5]]
//     Output: 2
// =============================================================

// Dijkstra with a simple priority queue using sort (acceptable for small inputs).
var minimumEffortPath = function(heights) {
    const R = heights.length, C = heights[0].length;
    const dist = Array.from({length:R}, () => new Array(C).fill(Infinity));
    dist[0][0] = 0;
    const pq = [[0,0,0]];
    while (pq.length) {
        pq.sort((a,b) => b[0]-a[0]);
        const [d, r, c] = pq.pop();
        if (r === R-1 && c === C-1) return d;
        if (d > dist[r][c]) continue;
        for (const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]) {
            const nr=r+dr, nc=c+dc;
            if (nr>=0&&nr<R&&nc>=0&&nc<C) {
                const nd = Math.max(d, Math.abs(heights[nr][nc]-heights[r][c]));
                if (nd < dist[nr][nc]) { dist[nr][nc] = nd; pq.push([nd,nr,nc]); }
            }
        }
    }
    return 0;
};
console.log(minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]));
