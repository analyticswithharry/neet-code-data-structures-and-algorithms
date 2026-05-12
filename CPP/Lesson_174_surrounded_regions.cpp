// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 174 -- Surrounded Regions
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 87
// =============================================================
//
// QUESTION:
//   Capture all 'O' regions surrounded by 'X' (regions touching the border are not captured).
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
int R,C; vector<vector<char>> B;
void dfs(int r,int c){if(r<0||r>=R||c<0||c>=C||B[r][c]!='O')return;B[r][c]='S';dfs(r+1,c);dfs(r-1,c);dfs(r,c+1);dfs(r,c-1);}
void solve(vector<vector<char>>& b){R=b.size();C=b[0].size();B=b;for(int r=0;r<R;r++){dfs(r,0);dfs(r,C-1);}for(int c=0;c<C;c++){dfs(0,c);dfs(R-1,c);}for(int r=0;r<R;r++)for(int c=0;c<C;c++)b[r][c]=B[r][c]=='S'?'O':'X';}
int main(){vector<vector<char>> g={{'X','X','X','X'},{'X','O','O','X'},{'X','X','O','X'},{'X','O','X','X'}};solve(g);for(auto& r:g){for(char x:r)cout<<x;cout<<"\n";}}
