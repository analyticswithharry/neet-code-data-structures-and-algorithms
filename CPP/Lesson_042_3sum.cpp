// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 042 -- 3Sum
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 21
// =============================================================
//
// QUESTION:
//   Given nums, return all unique triplets [a,b,c] such that a+b+c=0.
//
//   Example: [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
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
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end()); vector<vector<int>> res;
        for (int i=0;i<(int)nums.size()-2;i++) {
            if (i>0 && nums[i]==nums[i-1]) continue;
            int l=i+1, r=nums.size()-1;
            while (l<r) {
                int s = nums[i]+nums[l]+nums[r];
                if (s<0) l++;
                else if (s>0) r--;
                else {
                    res.push_back({nums[i],nums[l],nums[r]});
                    while (l<r && nums[l]==nums[l+1]) l++;
                    while (l<r && nums[r]==nums[r-1]) r--;
                    l++; r--;
                }
            }
        }
        return res;
    }
};
int main(){ vector<int> v={-1,0,1,2,-1,-4}; for (auto& t: Solution().threeSum(v)) { for (int x: t) cout<<x<<" "; cout<<"|"; } cout<<endl; }
