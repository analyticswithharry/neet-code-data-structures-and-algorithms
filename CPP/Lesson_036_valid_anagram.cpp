// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 036 -- Valid Anagram
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 18
// =============================================================
//
// QUESTION:
//   Given two strings s and t, return true if t is an anagram of s.
//
//   Example: s = "anagram", t = "nagaram" -> true
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
    bool isAnagram(string s, string t) {
        if (s.size()!=t.size()) return false;
        int c[26] = {0};
        for (size_t i=0;i<s.size();++i){ c[s[i]-'a']++; c[t[i]-'a']--; }
        for (int x: c) if (x) return false;
        return true;
    }
};
int main(){ Solution s; cout<<s.isAnagram("anagram","nagaram")<<" "<<s.isAnagram("rat","car")<<endl; }
