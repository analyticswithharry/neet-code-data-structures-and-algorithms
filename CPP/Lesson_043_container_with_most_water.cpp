// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 043 -- Container With Most Water
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 21
// =============================================================
//
// QUESTION:
//   Given heights, find two lines that with the x-axis form a container
//   holding the most water. Return the max area.
//
//   Example: [1,8,6,2,5,4,8,3,7] -> 49
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
    int maxArea(vector<int>& h) {
        int i=0, j=h.size()-1, best=0;
        while (i<j) {
            best = max(best, (j-i)*min(h[i],h[j]));
            if (h[i]<h[j]) i++; else j--;
        }
        return best;
    }
};
int main(){ vector<int> v={1,8,6,2,5,4,8,3,7}; cout<<Solution().maxArea(v)<<endl; }
