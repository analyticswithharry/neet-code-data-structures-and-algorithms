// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 018 -- Min Cost Climbing Stairs
// Category   : 1-D Dynamic Programming
// Difficulty : Easy
// Study Plan : Day 9
// =============================================================
//
// QUESTION:
//   You are given an integer array cost where cost[i] is the cost of i-th
//   step. Once you pay the cost, you can either climb one or two steps. You
//   can start from index 0 or 1. Return the minimum cost to reach the top.
//
//   Example:
//     Input : cost = [10,15,20]            Output: 15
//     Input : cost = [1,100,1,1,1,100,1,1,100,1]   Output: 6
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
    int minCostClimbingStairs(vector<int>& cost) {
        int a = 0, b = 0;
        for (int c : cost) { int t = min(a,b) + c; a = b; b = t; }
        return min(a, b);
    }
};
int main() {
    Solution s;
    vector<int> v1 = {10,15,20}, v2 = {1,100,1,1,1,100,1,1,100,1};
    cout << s.minCostClimbingStairs(v1) << " " << s.minCostClimbingStairs(v2) << endl;
}
