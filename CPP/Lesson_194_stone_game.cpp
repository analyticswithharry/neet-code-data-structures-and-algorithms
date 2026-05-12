// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 194 -- Stone Game
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 97
// =============================================================
//
// QUESTION:
//   Two players take stones from either end. Both play optimally. Return true if Alice wins.
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
bool stoneGame(vector<int> p){int n=p.size();vector<vector<int>> dp(n,vector<int>(n,0));for(int i=0;i<n;i++)dp[i][i]=p[i];for(int L=2;L<=n;L++)for(int i=0;i<=n-L;i++){int j=i+L-1;dp[i][j]=max(p[i]-dp[i+1][j],p[j]-dp[i][j-1]);}return dp[0][n-1]>0;}
int main(){cout<<boolalpha<<stoneGame({5,3,4,5})<<"\n";}
