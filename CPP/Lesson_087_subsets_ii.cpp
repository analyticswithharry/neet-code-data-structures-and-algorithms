// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 087 -- Subsets II
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 44
// =============================================================
//
// QUESTION:
//   Given an integer array nums that may contain duplicates, return all possible subsets (the power set), without duplicates.
//   Example: [1,2,2] -> [[],[1],[1,2],[1,2,2],[2],[2,2]].
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
    vector<vector<int>> res;
    void bt(vector<int>& nums, int i, vector<int>& cur){
        res.push_back(cur);
        for (int j=i;j<(int)nums.size();j++){
            if (j>i && nums[j]==nums[j-1]) continue;
            cur.push_back(nums[j]); bt(nums,j+1,cur); cur.pop_back();
        }
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums){
        sort(nums.begin(),nums.end()); vector<int> cur; bt(nums,0,cur); return res;
    }
};
int main(){ vector<int> a={1,2,2}; auto r=Solution().subsetsWithDup(a);
    for (auto& v: r){ cout<<"["; for(int x: v)cout<<x<<","; cout<<"] "; } cout<<endl; }
