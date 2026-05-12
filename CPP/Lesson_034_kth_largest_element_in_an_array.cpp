// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 034 -- Kth Largest Element In An Array
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 17
// =============================================================
//
// QUESTION:
//   Given an integer array nums and an integer k, return the kth largest
//   element in the array (the kth largest in sorted order, not the kth
//   distinct element).
//
//   Example:
//     Input : [3,2,1,5,6,4], k=2   Output: 5
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
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<>> pq;
        for (int n : nums) { pq.push(n); if ((int)pq.size() > k) pq.pop(); }
        return pq.top();
    }
};
int main() {
    vector<int> v = {3,2,1,5,6,4};
    cout << Solution().findKthLargest(v, 2) << endl;
}
