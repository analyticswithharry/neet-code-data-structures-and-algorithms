// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 098 -- Sort Colors
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 49
// =============================================================
//
// QUESTION:
//   Sort an array containing only 0, 1, 2 in-place (Dutch national flag).
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
    void sortColors(vector<int>& nums){
        int l=0, m=0, r=nums.size()-1;
        while (m<=r){
            if (nums[m]==0){ swap(nums[l],nums[m]); l++; m++; }
            else if (nums[m]==2){ swap(nums[r],nums[m]); r--; }
            else m++;
        }
    }
};
int main(){ vector<int> a={2,0,2,1,1,0}; Solution().sortColors(a);
    for (int x: a) cout<<x<<" "; cout<<endl; }
