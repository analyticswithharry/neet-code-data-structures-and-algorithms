// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 038 -- Top K Frequent Elements
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 19
// =============================================================
//
// QUESTION:
//   Given an integer array nums and integer k, return the k most frequent elements.
//
//   Example: nums = [1,1,1,2,2,3], k = 2 -> [1,2]
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
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> c;
        for (int n: nums) c[n]++;
        vector<pair<int,int>> v(c.begin(), c.end());
        sort(v.begin(), v.end(), [](auto& a, auto& b){return a.second>b.second;});
        vector<int> r; for (int i=0;i<k;i++) r.push_back(v[i].first); return r;
    }
};
int main(){ vector<int> v={1,1,1,2,2,3}; for (int x: Solution().topKFrequent(v,2)) cout<<x<<" "; cout<<endl; }
