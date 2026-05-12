// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 109 -- Best Time to Buy And Sell Stock
// Category   : Sliding Window
// Difficulty : Easy
// Study Plan : Day 55
// =============================================================
//
// QUESTION:
//   Given an array of stock prices where prices[i] is on day i, return the maximum profit from a single buy/sell. Return 0 if none.
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
class Solution { public:
    int maxProfit(vector<int>& prices){
        int lo=INT_MAX, best=0;
        for (int p: prices){ lo=min(lo,p); best=max(best, p-lo); }
        return best;
    }
};
int main(){ vector<int> p={7,1,5,3,6,4}; cout<<Solution().maxProfit(p)<<endl; }
