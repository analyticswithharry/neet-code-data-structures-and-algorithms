// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 201 -- Longest Increasing Path In a Matrix
// Category   : 2-D Dynamic Programming
// Difficulty : Hard
// Study Plan : Day 101
// =============================================================
//
// QUESTION:
//   Find length of the longest strictly-increasing path in a 2D grid.
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
int R,C; vector<vector<int>> G,M; int DIR[4][2]={{1,0},{-1,0},{0,1},{0,-1}};
int dfs(int r,int c){if(M[r][c])return M[r][c];int best=1;for(auto& d:DIR){int nr=r+d[0],nc=c+d[1];if(nr>=0&&nr<R&&nc>=0&&nc<C&&G[nr][nc]>G[r][c])best=max(best,1+dfs(nr,nc));}return M[r][c]=best;}
int longestIncreasingPath(vector<vector<int>> g){R=g.size();C=g[0].size();G=g;M.assign(R,vector<int>(C,0));int res=0;for(int r=0;r<R;r++)for(int c=0;c<C;c++)res=max(res,dfs(r,c));return res;}
int main(){cout<<longestIncreasingPath({{9,9,4},{6,6,8},{2,1,1}})<<"\n";}
