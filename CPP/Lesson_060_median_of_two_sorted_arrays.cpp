// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 060 -- Median of Two Sorted Arrays
// Category   : Binary Search
// Difficulty : Hard
// Study Plan : Day 30
// =============================================================
//
// QUESTION:
//   Given two sorted arrays nums1 and nums2, return the median of the
//   combined sorted array. Run in O(log(min(m,n))).
//
//   Example: [1,3], [2] -> 2.0
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
    double findMedianSortedArrays(vector<int>& a, vector<int>& b) {
        if (a.size() > b.size()) swap(a, b);
        int m = a.size(), n = b.size(), half = (m+n+1)/2;
        int lo = 0, hi = m;
        while (lo <= hi) {
            int i = (lo+hi)/2, j = half - i;
            int la = i>0 ? a[i-1] : INT_MIN;
            int ra = i<m ? a[i]   : INT_MAX;
            int lb = j>0 ? b[j-1] : INT_MIN;
            int rb = j<n ? b[j]   : INT_MAX;
            if (la <= rb && lb <= ra) {
                if ((m+n) % 2) return max(la, lb);
                return (max(la, lb) + min(ra, rb)) / 2.0;
            } else if (la > rb) hi = i-1;
            else lo = i+1;
        }
        return 0.0;
    }
};
int main(){ vector<int> a={1,3}, b={2}, c={1,2}, d={3,4};
    cout<<Solution().findMedianSortedArrays(a,b)<<" "<<Solution().findMedianSortedArrays(c,d)<<endl; }
