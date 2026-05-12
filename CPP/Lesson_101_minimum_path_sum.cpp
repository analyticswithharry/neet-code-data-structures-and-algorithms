// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 101 -- Minimum Path Sum
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 51
// =============================================================
//
// QUESTION:
//   Given an m x n grid filled with non-negative numbers, find the minimum path sum from top-left to bottom-right (only moves right or down).
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
    int minPathSum(vector<vector<int>>& g){
        int R=g.size(), C=g[0].size();
        for (int i=0;i<R;i++) for (int j=0;j<C;j++){
            if (i==0 && j==0) continue;
            if (i==0) g[i][j]+=g[i][j-1];
            else if (j==0) g[i][j]+=g[i-1][j];
            else g[i][j]+=min(g[i-1][j], g[i][j-1]);
        }
        return g[R-1][C-1];
    }
};
int main(){ vector<vector<int>> g={{1,3,1},{1,5,1},{4,2,1}}; cout<<Solution().minPathSum(g)<<endl; }
