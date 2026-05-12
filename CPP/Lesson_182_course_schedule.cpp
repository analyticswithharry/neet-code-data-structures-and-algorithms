// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 182 -- Course Schedule
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 91
// =============================================================
//
// QUESTION:
//   Given prerequisites pairs, can all courses be finished (no cycle)?
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
bool canFinish(int n,vector<vector<int>> pre){vector<vector<int>> g(n);vector<int> ind(n,0);for(auto& p:pre){g[p[1]].push_back(p[0]);ind[p[0]]++;}queue<int> q;for(int i=0;i<n;i++) if(ind[i]==0)q.push(i);int cnt=0;while(!q.empty()){int x=q.front();q.pop();cnt++;for(int y:g[x]) if(--ind[y]==0)q.push(y);}return cnt==n;}
int main(){cout<<boolalpha<<canFinish(2,{{1,0}})<<"\n"<<canFinish(2,{{1,0},{0,1}})<<"\n";}
