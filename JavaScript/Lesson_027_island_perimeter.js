// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 027 -- Island Perimeter
// Category   : Graphs
// Difficulty : Easy
// Study Plan : Day 14
// =============================================================
//
// QUESTION:
//   Given an m x n grid where 1 represents land and 0 water, return the
//   perimeter of the island (the grid is completely surrounded by water and
//   there is exactly one island).
//
//   Example:
//     Input : grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
//     Output: 16
// =============================================================

var islandPerimeter = function(grid) {
    const R = grid.length, C = grid[0].length; let p = 0;
    for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) if (grid[r][c] === 1) {
        p += 4;
        if (r && grid[r-1][c] === 1) p -= 2;
        if (c && grid[r][c-1] === 1) p -= 2;
    }
    return p;
};
console.log(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]));
