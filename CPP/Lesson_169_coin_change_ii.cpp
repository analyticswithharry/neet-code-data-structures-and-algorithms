// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 169 -- Coin Change II
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 85
// =============================================================
//
// QUESTION:
//   Number of distinct combinations of coins (unlimited) summing to amount.
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
int change(int amt,vector<int> coins){vector<long long> dp(amt+1,0);dp[0]=1;for(int c:coins) for(int a=c;a<=amt;a++) dp[a]+=dp[a-c];return (int)dp[amt];}
int main(){cout<<change(5,{1,2,5})<<"\n"<<change(3,{2})<<"\n";}
