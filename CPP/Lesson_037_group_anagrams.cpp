// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 037 -- Group Anagrams
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 18
// =============================================================
//
// QUESTION:
//   Given an array of strings strs, group the anagrams together.
//
//   Example: ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"],["tan","nat"],["bat"]]
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
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> m;
        for (auto& s: strs) { string k=s; sort(k.begin(),k.end()); m[k].push_back(s); }
        vector<vector<string>> r; for (auto& p: m) r.push_back(p.second); return r;
    }
};
int main(){ vector<string> v={"eat","tea","tan","ate","nat","bat"}; auto r=Solution().groupAnagrams(v);
    for(auto& g:r){ for(auto& s:g) cout<<s<<" "; cout<<"|"; } cout<<endl; }
