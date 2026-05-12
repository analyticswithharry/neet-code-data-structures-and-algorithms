// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 103 -- Merge Intervals
// Category   : Intervals
// Difficulty : Medium
// Study Plan : Day 52
// =============================================================
//
// QUESTION:
//   Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals.
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
    vector<vector<int>> merge(vector<vector<int>>& intervals){
        sort(intervals.begin(), intervals.end()); vector<vector<int>> res;
        for (auto& x: intervals){
            if (!res.empty() && x[0]<=res.back()[1]) res.back()[1]=max(res.back()[1], x[1]);
            else res.push_back(x);
        }
        return res;
    }
};
int main(){ vector<vector<int>> v={{1,3},{2,6},{8,10},{15,18}};
    for (auto& r: Solution().merge(v)){ cout<<"["<<r[0]<<","<<r[1]<<"] "; } cout<<endl; }
