// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 200 -- Edit Distance
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 100
// =============================================================
//
// QUESTION:
//   Min number of insert/delete/replace ops to convert s1 to s2.
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
int minDistance(string a,string b){int m=a.size(),n=b.size();vector<vector<int>> dp(m+1,vector<int>(n+1,0));for(int i=0;i<=m;i++)dp[i][0]=i;for(int j=0;j<=n;j++)dp[0][j]=j;for(int i=1;i<=m;i++)for(int j=1;j<=n;j++){if(a[i-1]==b[j-1])dp[i][j]=dp[i-1][j-1];else dp[i][j]=1+min({dp[i-1][j],dp[i][j-1],dp[i-1][j-1]});}return dp[m][n];}
int main(){cout<<minDistance("horse","ros")<<"\n"<<minDistance("intention","execution")<<"\n";}
