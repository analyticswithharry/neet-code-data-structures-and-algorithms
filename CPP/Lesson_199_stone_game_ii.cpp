// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 199 -- Stone Game II
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 100
// =============================================================
//
// QUESTION:
//   Two players take stones from front; can take X piles where 1<=X<=2M (M starts at 1). Maximize own.
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
vector<int> SUF; int N; vector<vector<int>> MM;
int dfs(int i,int m){if(i+2*m>=N)return SUF[i];if(MM[i][m]!=-1)return MM[i][m];int best=0;for(int x=1;x<=2*m;x++)best=max(best,SUF[i]-dfs(i+x,max(m,x)));return MM[i][m]=best;}
int stoneGameII(vector<int> p){N=p.size();SUF.assign(N+1,0);for(int i=N-1;i>=0;i--)SUF[i]=SUF[i+1]+p[i];MM.assign(N+1,vector<int>(N+1,-1));return dfs(0,1);}
int main(){cout<<stoneGameII({2,7,9,4,4})<<"\n";}
