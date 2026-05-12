// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 178 -- Longest Increasing Subsequence
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 89
// =============================================================
//
// QUESTION:
//   Length of the longest strictly-increasing subsequence.
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
int LIS(vector<int> a){vector<int> t;for(int x:a){auto it=lower_bound(t.begin(),t.end(),x);if(it==t.end())t.push_back(x);else *it=x;}return t.size();}
int main(){cout<<LIS({10,9,2,5,3,7,101,18})<<"\n"<<LIS({0,1,0,3,2,3})<<"\n";}
