// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 019 -- Kth Largest Element In a Stream
// Category   : Heap Priority Queue
// Difficulty : Easy
// Study Plan : Day 10
// =============================================================
//
// QUESTION:
//   Design a class to find the kth largest element in a stream. Implement:
//     KthLargest(int k, int[] nums)
//     add(val) -> returns the element representing the kth largest in the stream.
//
//   Example:
//     k=3, nums=[4,5,8,2]
//     add(3) -> 4; add(5) -> 5; add(10) -> 5; add(9) -> 8; add(4) -> 8
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
class KthLargest {
    priority_queue<int, vector<int>, greater<int>> pq;
    int k;
public:
    KthLargest(int k, vector<int>& nums) : k(k) { for (int n : nums) add(n); }
    int add(int val) {
        if ((int)pq.size() < k) pq.push(val);
        else if (val > pq.top()) { pq.pop(); pq.push(val); }
        return pq.top();
    }
};
int main() {
    vector<int> v = {4,5,8,2}; KthLargest kl(3, v);
    for (int x : {3,5,10,9,4}) cout << kl.add(x) << " ";
    cout << endl;
}
