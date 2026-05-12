// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 048 -- Permutation in String
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 24
// =============================================================
//
// QUESTION:
//   Given s1 and s2, return true if s2 contains a permutation of s1.
//
//   Example: s1="ab", s2="eidbaooo" -> true
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
    bool checkInclusion(string s1, string s2) {
        if (s1.size()>s2.size()) return false;
        int a[26]={0}, b[26]={0};
        for (size_t i=0;i<s1.size();i++) { a[s1[i]-'a']++; b[s2[i]-'a']++; }
        auto eq = [&](){ for (int i=0;i<26;i++) if (a[i]!=b[i]) return false; return true; };
        if (eq()) return true;
        for (size_t i=s1.size();i<s2.size();i++) {
            b[s2[i]-'a']++;
            b[s2[i-s1.size()]-'a']--;
            if (eq()) return true;
        }
        return false;
    }
};
int main(){ Solution s; cout<<s.checkInclusion("ab","eidbaooo")<<" "<<s.checkInclusion("ab","eidboaoo")<<endl; }
