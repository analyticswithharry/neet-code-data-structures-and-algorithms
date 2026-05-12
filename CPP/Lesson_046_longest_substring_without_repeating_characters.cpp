// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 046 -- Longest Substring Without Repeating Characters
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 23
// =============================================================
//
// QUESTION:
//   Given a string, find the length of the longest substring without
//   repeating characters.
//
//   Example: "abcabcbb" -> 3
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
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> seen; int l=0, best=0;
        for (int r=0;r<(int)s.size();r++) {
            auto it = seen.find(s[r]);
            if (it!=seen.end() && it->second>=l) l = it->second+1;
            seen[s[r]] = r;
            best = max(best, r-l+1);
        }
        return best;
    }
};
int main(){ Solution s; cout<<s.lengthOfLongestSubstring("abcabcbb")<<" "<<s.lengthOfLongestSubstring("bbbbb")<<endl; }
