// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 032 -- Unique Paths II
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 16
// =============================================================
//
// QUESTION:
//   You are given an m x n integer array obstacleGrid. There is a robot
//   at the top-left. It moves right or down. An obstacle is marked as 1; an
//   empty space as 0. Return the number of possible unique paths to the
//   bottom-right corner.
//
//   Example:
//     Input : [[0,0,0],[0,1,0],[0,0,0]]   Output: 2
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
    int uniquePathsWithObstacles(vector<vector<int>>& g) {
        int R = g.size(), C = g[0].size();
        if (g[0][0]) return 0;
        vector<long long> dp(C, 0); dp[0] = 1;
        for (int r = 0; r < R; ++r) {
            if (g[r][0]) dp[0] = 0;
            for (int c = 1; c < C; ++c) dp[c] = g[r][c] ? 0 : dp[c] + dp[c-1];
        }
        return (int)dp[C-1];
    }
};
int main() {
    vector<vector<int>> g = {{0,0,0},{0,1,0},{0,0,0}};
    cout << Solution().uniquePathsWithObstacles(g) << endl;
}
