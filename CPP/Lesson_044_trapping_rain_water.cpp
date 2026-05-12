// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 044 -- Trapping Rain Water
// Category   : Two Pointers
// Difficulty : Hard
// Study Plan : Day 22
// =============================================================
//
// QUESTION:
//   Given heights, compute how much water can be trapped after raining.
//
//   Example: [0,1,0,2,1,0,1,3,2,1,2,1] -> 6
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
    int trap(vector<int>& h) {
        int l=0, r=h.size()-1, lm=0, rm=0, ans=0;
        while (l<r) {
            if (h[l]<h[r]) { lm=max(lm,h[l]); ans+=lm-h[l]; l++; }
            else { rm=max(rm,h[r]); ans+=rm-h[r]; r--; }
        }
        return ans;
    }
};
int main(){ vector<int> v={0,1,0,2,1,0,1,3,2,1,2,1}; cout<<Solution().trap(v)<<endl; }
