// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 203 -- Course Schedule II
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 102
// =============================================================
//
// QUESTION:
//   Return any topological ordering of courses, or empty array if impossible.
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
vector<int> findOrder(int n,vector<vector<int>> pre){vector<vector<int>> g(n);vector<int> ind(n,0);for(auto& p:pre){g[p[1]].push_back(p[0]);ind[p[0]]++;}queue<int> q;for(int i=0;i<n;i++) if(ind[i]==0)q.push(i);vector<int> res;while(!q.empty()){int x=q.front();q.pop();res.push_back(x);for(int y:g[x]) if(--ind[y]==0)q.push(y);}return (int)res.size()==n?res:vector<int>{};}
int main(){auto r=findOrder(4,{{1,0},{2,0},{3,1},{3,2}});for(int x:r)cout<<x<<" ";cout<<"\n";}
