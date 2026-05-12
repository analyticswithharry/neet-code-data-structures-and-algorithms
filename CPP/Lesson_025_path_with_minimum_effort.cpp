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
    int minimumEffortPath(vector<vector<int>>& h) {
        int R = h.size(), C = h[0].size();
        vector<vector<int>> dist(R, vector<int>(C, INT_MAX));
        dist[0][0] = 0;
        priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, greater<>> pq;
        pq.push({0,0,0});
        int D[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!pq.empty()) {
            auto [d, r, c] = pq.top(); pq.pop();
            if (r==R-1 && c==C-1) return d;
            if (d > dist[r][c]) continue;
            for (auto& dd : D) {
                int nr=r+dd[0], nc=c+dd[1];
                if (nr>=0&&nr<R&&nc>=0&&nc<C) {
                    int nd = max(d, abs(h[nr][nc]-h[r][c]));
                    if (nd < dist[nr][nc]) { dist[nr][nc] = nd; pq.push({nd,nr,nc}); }
                }
            }
        }
        return 0;
    }
};
int main() {
    vector<vector<int>> h = {{1,2,2},{3,8,2},{5,3,5}};
    cout << Solution().minimumEffortPath(h) << endl;
}
