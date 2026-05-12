// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 167 -- Coin Change
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 84
// =============================================================
//
// QUESTION:
//   Fewest coins needed to make up amount; coins are unlimited. Return -1 if impossible.
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
int coinChange(vector<int> coins,int amt){int INF=1e9;vector<int> dp(amt+1,INF);dp[0]=0;for(int a=1;a<=amt;a++)for(int c:coins) if(c<=a) dp[a]=min(dp[a],dp[a-c]+1);return dp[amt]>=INF?-1:dp[amt];}
int main(){cout<<coinChange({1,2,5},11)<<"\n"<<coinChange({2},3)<<"\n";}
