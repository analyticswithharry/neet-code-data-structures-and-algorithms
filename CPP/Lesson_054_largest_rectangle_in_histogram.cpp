// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 054 -- Largest Rectangle in Histogram
// Category   : Stack
// Difficulty : Hard
// Study Plan : Day 27
// =============================================================
//
// QUESTION:
//   Given heights of bars, find the area of the largest rectangle.
//
//   Example: [2,1,5,6,2,3] -> 10
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
    int largestRectangleArea(vector<int>& h) {
        stack<pair<int,int>> st; int best = 0; int n = h.size();
        for (int i=0;i<=n;i++) {
            int v = (i==n) ? 0 : h[i];
            int start = i;
            while (!st.empty() && st.top().second > v) {
                auto [idx, ht] = st.top(); st.pop();
                best = max(best, ht*(i-idx));
                start = idx;
            }
            st.push({start, v});
        }
        return best;
    }
};
int main(){ vector<int> v={2,1,5,6,2,3}; cout<<Solution().largestRectangleArea(v)<<endl; }
