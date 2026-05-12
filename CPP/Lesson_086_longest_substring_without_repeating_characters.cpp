// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 086 -- Longest Substring Without Repeating Characters
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 43
// =============================================================
//
// QUESTION:
//   Given a string s, find the length of the longest substring without repeating characters.
//   Example: 'abcabcbb' -> 3 ('abc'); 'bbbbb' -> 1; 'pwwkew' -> 3.
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
    int lengthOfLongestSubstring(string s){
        unordered_map<char,int> m; int l=0, best=0;
        for (int r=0;r<(int)s.size();r++){
            char c=s[r];
            if (m.count(c) && m[c]>=l) l = m[c]+1;
            m[c]=r; best = max(best, r-l+1);
        } return best;
    }
};
int main(){ Solution s; cout<<s.lengthOfLongestSubstring("abcabcbb")<<" "<<s.lengthOfLongestSubstring("pwwkew")<<endl; }
