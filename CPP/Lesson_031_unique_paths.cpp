// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 031 -- Unique Paths
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 16
// =============================================================
//
// QUESTION:
//   A robot is on an m x n grid at the top-left. It can only move right or
//   down. How many possible unique paths are there to reach the bottom-right?
//
//   Example:
//     Input : m=3, n=7  Output: 28
//     Input : m=3, n=2  Output: 3
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
    int uniquePaths(int m, int n) {
        vector<int> dp(n, 1);
        for (int i = 1; i < m; ++i) for (int j = 1; j < n; ++j) dp[j] += dp[j-1];
        return dp[n-1];
    }
};
int main() { Solution s; cout << s.uniquePaths(3,7) << " " << s.uniquePaths(3,2) << endl; }
