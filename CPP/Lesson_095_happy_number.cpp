// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 095 -- Happy Number
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 48
// =============================================================
//
// QUESTION:
//   A number is happy if repeatedly summing the squares of its digits eventually equals 1. Return true if n is happy.
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
    bool isHappy(int n){
        unordered_set<int> seen;
        while (n!=1 && !seen.count(n)){
            seen.insert(n); int s=0;
            while (n>0){ int d=n%10; s+=d*d; n/=10; } n=s;
        }
        return n==1;
    }
};
int main(){ Solution s; cout<<s.isHappy(19)<<" "<<s.isHappy(2)<<endl; }
