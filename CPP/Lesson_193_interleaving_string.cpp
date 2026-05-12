// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 193 -- Interleaving String
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 97
// =============================================================
//
// QUESTION:
//   Determine whether s3 can be formed by interleaving s1 and s2.
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
bool isInterleave(string a,string b,string c){if(a.size()+b.size()!=c.size())return false;vector<vector<bool>> dp(a.size()+1,vector<bool>(b.size()+1,false));dp[0][0]=true;for(int i=0;i<=(int)a.size();i++)for(int j=0;j<=(int)b.size();j++){if(i&&a[i-1]==c[i+j-1])dp[i][j]=dp[i][j]||dp[i-1][j];if(j&&b[j-1]==c[i+j-1])dp[i][j]=dp[i][j]||dp[i][j-1];}return dp[a.size()][b.size()];}
int main(){cout<<boolalpha<<isInterleave("aabcc","dbbca","aadbbcbcac")<<"\n"<<isInterleave("aabcc","dbbca","aadbbbaccc")<<"\n";}
