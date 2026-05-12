// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 057 -- Find Minimum in Rotated Sorted Array
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 28
// =============================================================
//
// QUESTION:
//   Given a rotated sorted array of unique elements, return its minimum.
//
//   Example: [3,4,5,1,2] -> 1
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
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int mid = (l+r)/2;
            if (nums[mid] > nums[r]) l = mid+1; else r = mid;
        }
        return nums[l];
    }
};
int main(){ vector<int> v={3,4,5,1,2}, w={4,5,6,7,0,1,2}; cout<<Solution().findMin(v)<<" "<<Solution().findMin(w)<<endl; }
