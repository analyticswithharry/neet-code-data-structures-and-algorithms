// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 104 -- Non Overlapping Intervals
// Category   : Intervals
// Difficulty : Medium
// Study Plan : Day 52
// =============================================================
//
// QUESTION:
//   Given an array of intervals, return the minimum number of intervals to remove so the rest are non-overlapping.
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
    int eraseOverlapIntervals(vector<vector<int>>& intervals){
        sort(intervals.begin(), intervals.end(), [](auto&a, auto&b){return a[1]<b[1];});
        int end=INT_MIN, rm=0;
        for (auto& x: intervals){ if (x[0]>=end) end=x[1]; else rm++; }
        return rm;
    }
};
int main(){ vector<vector<int>> v={{1,2},{2,3},{3,4},{1,3}}; cout<<Solution().eraseOverlapIntervals(v)<<endl; }
