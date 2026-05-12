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
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<int, vector<int>>> pq;
        for (auto& p : points) {
            int d = p[0]*p[0] + p[1]*p[1];
            pq.push({d, p});
            if ((int)pq.size() > k) pq.pop();
        }
        vector<vector<int>> out;
        while (!pq.empty()) { out.push_back(pq.top().second); pq.pop(); }
        return out;
    }
};
int main() {
    vector<vector<int>> v = {{3,3},{5,-1},{-2,4}};
    for (auto& p : Solution().kClosest(v, 2)) cout << p[0] << "," << p[1] << " ";
    cout << endl;
}
