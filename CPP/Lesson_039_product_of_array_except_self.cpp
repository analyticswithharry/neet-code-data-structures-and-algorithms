// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 039 -- Product of Array Except Self
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 19
// =============================================================
//
// QUESTION:
//   Given nums, return an array where answer[i] is the product of all elements
//   except nums[i]. Must run in O(n) without division.
//
//   Example: [1,2,3,4] -> [24,12,8,6]
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
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size(); vector<int> r(n,1);
        int left = 1;
        for (int i=0;i<n;i++){ r[i]=left; left*=nums[i]; }
        int right = 1;
        for (int i=n-1;i>=0;i--){ r[i]*=right; right*=nums[i]; }
        return r;
    }
};
int main(){ vector<int> v={1,2,3,4}; for (int x: Solution().productExceptSelf(v)) cout<<x<<" "; cout<<endl; }
