// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 105 -- Merge Strings Alternately
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 53
// =============================================================
//
// QUESTION:
//   Given two strings, merge them by adding letters in alternating order, starting with word1. If one is longer, append the rest.
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
    string mergeAlternately(string a, string b){
        string r; int i=0;
        while (i<(int)a.size() || i<(int)b.size()){
            if (i<(int)a.size()) r+=a[i];
            if (i<(int)b.size()) r+=b[i];
            i++;
        }
        return r;
    }
};
int main(){ Solution s; cout<<s.mergeAlternately("abc","pqr")<<" "<<s.mergeAlternately("ab","pqrs")<<endl; }
