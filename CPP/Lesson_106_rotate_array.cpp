// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 106 -- Rotate Array
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 53
// =============================================================
//
// QUESTION:
//   Rotate the array to the right by k steps in-place.
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
    void rotate(vector<int>& nums, int k){
        int n=nums.size(); k%=n;
        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.begin()+k);
        reverse(nums.begin()+k, nums.end());
    }
};
int main(){ vector<int> a={1,2,3,4,5,6,7}; Solution().rotate(a, 3);
    for (int x: a) cout<<x<<" "; cout<<endl; }
