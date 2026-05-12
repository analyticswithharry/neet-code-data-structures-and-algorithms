// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 097 -- Majority Element
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 49
// =============================================================
//
// QUESTION:
//   Given an array of size n, return the element that appears more than n/2 times.
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
    int majorityElement(vector<int>& nums){
        int cand=0, cnt=0;
        for (int n: nums){ if (cnt==0) cand=n; cnt += n==cand?1:-1; }
        return cand;
    }
};
int main(){ vector<int> a={3,2,3}, b={2,2,1,1,1,2,2};
    cout<<Solution().majorityElement(a)<<" "<<Solution().majorityElement(b)<<endl; }
