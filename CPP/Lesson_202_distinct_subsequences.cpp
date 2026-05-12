// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 202 -- Distinct Subsequences
// Category   : 2-D Dynamic Programming
// Difficulty : Hard
// Study Plan : Day 101
// =============================================================
//
// QUESTION:
//   Number of distinct subsequences of s equal to t.
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
int numDistinct(string s,string t){int m=s.size(),n=t.size();vector<vector<long long>> dp(m+1,vector<long long>(n+1,0));for(int i=0;i<=m;i++)dp[i][0]=1;for(int i=1;i<=m;i++)for(int j=1;j<=n;j++){dp[i][j]=dp[i-1][j]+(s[i-1]==t[j-1]?dp[i-1][j-1]:0);}return (int)dp[m][n];}
int main(){cout<<numDistinct("rabbbit","rabbit")<<"\n";}
