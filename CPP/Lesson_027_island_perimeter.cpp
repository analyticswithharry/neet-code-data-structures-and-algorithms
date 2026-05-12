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

#include <vector>
#include <string>
#include <iostream>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <algorithm>
#include <climits>
#include <numeric>
#include <functional>
#include <cmath>
using namespace std;
class Solution {
public:
    int islandPerimeter(vector<vector<int>>& g) {
        int R = g.size(), C = g[0].size(), p = 0;
        for (int r = 0; r < R; ++r) for (int c = 0; c < C; ++c) if (g[r][c] == 1) {
            p += 4;
            if (r > 0 && g[r-1][c] == 1) p -= 2;
            if (c > 0 && g[r][c-1] == 1) p -= 2;
        }
        return p;
    }
};
int main() {
    vector<vector<int>> g = {{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}};
    cout << Solution().islandPerimeter(g) << endl;
}
