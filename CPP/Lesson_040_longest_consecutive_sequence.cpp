// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 040 -- Longest Consecutive Sequence
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 20
// =============================================================
//
// QUESTION:
//   Given an unsorted array, return the length of the longest consecutive
//   elements sequence in O(n).
//
//   Example: [100,4,200,1,3,2] -> 4 (sequence 1,2,3,4)
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
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end()); int best = 0;
        for (int n: s) if (!s.count(n-1)) {
            int cur = n, len = 1;
            while (s.count(cur+1)) { cur++; len++; }
            best = max(best, len);
        }
        return best;
    }
};
int main(){ vector<int> v={100,4,200,1,3,2}; cout<<Solution().longestConsecutive(v)<<endl; }
