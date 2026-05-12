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
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int,int>>> g(n+1);
        for (auto& t : times) g[t[0]].push_back({t[1], t[2]});
        vector<int> dist(n+1, INT_MAX); dist[k] = 0;
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
        pq.push({0, k});
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d > dist[u]) continue;
            for (auto& [v, w] : g[u]) if (d + w < dist[v]) { dist[v] = d + w; pq.push({dist[v], v}); }
        }
        int mx = 0;
        for (int i = 1; i <= n; ++i) { if (dist[i] == INT_MAX) return -1; mx = max(mx, dist[i]); }
        return mx;
    }
};
int main() {
    vector<vector<int>> t = {{2,1,1},{2,3,1},{3,4,1}};
    cout << Solution().networkDelayTime(t, 4, 2) << endl;
}
