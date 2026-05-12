// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 052 -- Daily Temperatures
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 26
// =============================================================
//
// QUESTION:
//   Given temperatures, for each day return the number of days until a
//   warmer temperature, or 0 if none.
//
//   Example: [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
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
    vector<int> dailyTemperatures(vector<int>& t) {
        int n = t.size(); vector<int> res(n,0); stack<int> st;
        for (int i=0;i<n;i++) {
            while (!st.empty() && t[st.top()] < t[i]) {
                int j = st.top(); st.pop(); res[j] = i - j;
            }
            st.push(i);
        }
        return res;
    }
};
int main(){ vector<int> v={73,74,75,71,69,72,76,73}; for (int x: Solution().dailyTemperatures(v)) cout<<x<<" "; cout<<endl; }
