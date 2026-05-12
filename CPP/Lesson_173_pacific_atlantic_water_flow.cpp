// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 173 -- Pacific Atlantic Water Flow
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 87
// =============================================================
//
// QUESTION:
//   Return cells from which water can flow to both Pacific (top/left) and Atlantic (bottom/right).
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
int R,C; vector<vector<int>> H; int DIR[4][2]={{1,0},{-1,0},{0,1},{0,-1}};
void dfs(int r,int c,vector<vector<bool>>& s){s[r][c]=true;for(auto& d:DIR){int nr=r+d[0],nc=c+d[1];if(nr>=0&&nr<R&&nc>=0&&nc<C&&!s[nr][nc]&&H[nr][nc]>=H[r][c])dfs(nr,nc,s);}}
vector<vector<int>> pacificAtlantic(vector<vector<int>> h){R=h.size();C=h[0].size();H=h;vector<vector<bool>> pac(R,vector<bool>(C,false)),atl(R,vector<bool>(C,false));for(int c=0;c<C;c++){dfs(0,c,pac);dfs(R-1,c,atl);}for(int r=0;r<R;r++){dfs(r,0,pac);dfs(r,C-1,atl);}vector<vector<int>> res;for(int r=0;r<R;r++)for(int c=0;c<C;c++)if(pac[r][c]&&atl[r][c])res.push_back({r,c});return res;}
int main(){cout<<pacificAtlantic({{1,2,2,3,5},{3,2,3,4,4},{2,4,5,3,1},{6,7,1,4,5},{5,1,1,2,4}}).size()<<"\n";}
