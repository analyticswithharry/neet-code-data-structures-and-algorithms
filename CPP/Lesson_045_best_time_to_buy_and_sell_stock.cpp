// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 045 -- Best Time to Buy and Sell Stock
// Category   : Sliding Window
// Difficulty : Easy
// Study Plan : Day 22
// =============================================================
//
// QUESTION:
//   Given prices, return the maximum profit from a single buy/sell.
//
//   Example: [7,1,5,3,6,4] -> 5
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
    int maxProfit(vector<int>& prices) {
        int lo = INT_MAX, best = 0;
        for (int p: prices) { if (p<lo) lo=p; else if (p-lo>best) best=p-lo; }
        return best;
    }
};
int main(){ vector<int> v={7,1,5,3,6,4}; cout<<Solution().maxProfit(v)<<endl; }
