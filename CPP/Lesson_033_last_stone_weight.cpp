// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 033 -- Last Stone Weight
// Category   : Heap Priority Queue
// Difficulty : Easy
// Study Plan : Day 17
// =============================================================
//
// QUESTION:
//   You are given an array of stones. On each turn pick the two heaviest
//   stones x <= y. If x == y both are destroyed; if x != y, x is destroyed
//   and y becomes y - x. Return the weight of the last remaining stone (or 0).
//
//   Example:
//     Input : [2,7,4,1,8,1]   Output: 1
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
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq(stones.begin(), stones.end());
        while (pq.size() > 1) {
            int y = pq.top(); pq.pop(); int x = pq.top(); pq.pop();
            if (y != x) pq.push(y - x);
        }
        return pq.empty() ? 0 : pq.top();
    }
};
int main() {
    vector<int> v = {2,7,4,1,8,1};
    cout << Solution().lastStoneWeight(v) << endl;
}
