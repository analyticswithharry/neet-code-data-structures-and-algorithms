// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 058 -- Search in Rotated Sorted Array
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 29
// =============================================================
//
// QUESTION:
//   Search target in a rotated sorted array of unique values.
//   Return its index, or -1 if not found.
//
//   Example: nums=[4,5,6,7,0,1,2], target=0 -> 4
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
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int mid = (l+r)/2;
            if (nums[mid] == target) return mid;
            if (nums[l] <= nums[mid]) {
                if (nums[l] <= target && target < nums[mid]) r = mid-1;
                else l = mid+1;
            } else {
                if (nums[mid] < target && target <= nums[r]) l = mid+1;
                else r = mid-1;
            }
        }
        return -1;
    }
};
int main(){ vector<int> v={4,5,6,7,0,1,2}; cout<<Solution().search(v,0)<<" "<<Solution().search(v,3)<<endl; }
