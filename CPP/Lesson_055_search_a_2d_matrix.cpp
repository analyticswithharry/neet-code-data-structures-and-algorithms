// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 055 -- Search a 2D Matrix
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 27
// =============================================================
//
// QUESTION:
//   Given an m x n matrix sorted row-wise (and each row's first > prev row's last),
//   search for target.
//
//   Example: [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3 -> true
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
    bool searchMatrix(vector<vector<int>>& m, int target) {
        if (m.empty() || m[0].empty()) return false;
        int rows = m.size(), cols = m[0].size();
        int l = 0, r = rows*cols - 1;
        while (l <= r) {
            int mid = (l+r)/2;
            int v = m[mid/cols][mid%cols];
            if (v == target) return true;
            if (v < target) l = mid+1; else r = mid-1;
        }
        return false;
    }
};
int main(){ vector<vector<int>> m = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
    cout<<Solution().searchMatrix(m,3)<<" "<<Solution().searchMatrix(m,13)<<endl; }
