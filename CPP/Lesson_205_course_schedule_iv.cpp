// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 205 -- Course Schedule IV
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 103
// =============================================================
//
// QUESTION:
//   Given prerequisites, answer queries: is course u a (transitive) prerequisite of v?
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
vector<bool> checkIfPrerequisite(int n,vector<vector<int>> pre,vector<vector<int>> qs){vector<vector<bool>> r(n,vector<bool>(n,false));vector<vector<int>> g(n);vector<int> ind(n,0);for(auto& p:pre){g[p[0]].push_back(p[1]);ind[p[1]]++;r[p[0]][p[1]]=true;}queue<int> q;for(int i=0;i<n;i++) if(ind[i]==0)q.push(i);vector<int> order;while(!q.empty()){int x=q.front();q.pop();order.push_back(x);for(int y:g[x]) if(--ind[y]==0)q.push(y);}for(int x:order) for(int y:g[x]) for(int k=0;k<n;k++) if(r[k][x])r[k][y]=true;vector<bool> out;for(auto& qq:qs)out.push_back(r[qq[0]][qq[1]]);return out;}
int main(){auto r=checkIfPrerequisite(3,{{1,2},{1,0},{2,0}},{{1,0},{1,2}});for(bool b:r)cout<<b<<" ";cout<<"\n";}
