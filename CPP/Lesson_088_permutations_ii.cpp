// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 088 -- Permutations II
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 44
// =============================================================
//
// QUESTION:
//   Given a collection nums of numbers that might contain duplicates, return all possible unique permutations.
//   Example: [1,1,2] -> [[1,1,2],[1,2,1],[2,1,1]].
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
    vector<vector<int>> res; vector<bool> used; vector<int> cur;
    void bt(vector<int>& nums){
        if (cur.size()==nums.size()){ res.push_back(cur); return; }
        for (int i=0;i<(int)nums.size();i++){
            if (used[i]) continue;
            if (i>0 && nums[i]==nums[i-1] && !used[i-1]) continue;
            used[i]=true; cur.push_back(nums[i]); bt(nums);
            cur.pop_back(); used[i]=false;
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums){
        sort(nums.begin(),nums.end()); used.assign(nums.size(),false); bt(nums); return res;
    }
};
int main(){ vector<int> a={1,1,2}; auto r=Solution().permuteUnique(a);
    for (auto& v: r){ cout<<"["; for(int x: v)cout<<x<<","; cout<<"] "; } cout<<endl; }
