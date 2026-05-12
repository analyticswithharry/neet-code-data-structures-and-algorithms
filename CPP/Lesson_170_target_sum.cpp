// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 170 -- Target Sum
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 85
// =============================================================
//
// QUESTION:
//   Assign + or - to each number so the sum equals target. Return number of ways.
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
int findTargetSumWays(vector<int> nums,int target){unordered_map<int,int> dp;dp[0]=1;for(int n:nums){unordered_map<int,int> nd;for(auto& p:dp){nd[p.first+n]+=p.second;nd[p.first-n]+=p.second;}dp=nd;}return dp.count(target)?dp[target]:0;}
int main(){cout<<findTargetSumWays({1,1,1,1,1},3)<<"\n";}
