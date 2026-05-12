// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 096 -- Rotate Image
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 48
// =============================================================
//
// QUESTION:
//   Rotate an n x n 2D matrix 90 degrees clockwise in-place.
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
    void rotate(vector<vector<int>>& m){
        int n=m.size();
        for (int i=0;i<n;i++) for (int j=i+1;j<n;j++) swap(m[i][j], m[j][i]);
        for (auto& r: m) reverse(r.begin(), r.end());
    }
};
int main(){ vector<vector<int>> m={{1,2,3},{4,5,6},{7,8,9}}; Solution().rotate(m);
    for (auto& r: m){ for (int x: r) cout<<x<<" "; cout<<endl; } }
