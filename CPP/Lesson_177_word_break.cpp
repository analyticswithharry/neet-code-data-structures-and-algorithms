// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 177 -- Word Break
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 89
// =============================================================
//
// QUESTION:
//   Determine if string s can be segmented into words from the given dictionary.
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
bool wordBreak(string s,vector<string> wd){unordered_set<string> w(wd.begin(),wd.end());int n=s.size();vector<bool> dp(n+1,false);dp[0]=true;for(int i=1;i<=n;i++)for(int j=0;j<i;j++)if(dp[j]&&w.count(s.substr(j,i-j))){dp[i]=true;break;}return dp[n];}
int main(){cout<<boolalpha<<wordBreak("leetcode",{"leet","code"})<<"\n"<<wordBreak("catsandog",{"cats","dog","sand","and","cat"})<<"\n";}
