// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 206 -- Number of Connected Components In An Undirected Graph
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 103
// =============================================================
//
// QUESTION:
//   Given n nodes and undirected edges, return the number of connected components.
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
vector<int> P; int find(int x){while(P[x]!=x){P[x]=P[P[x]];x=P[x];}return x;}
int countComponents(int n,vector<vector<int>> e){P.resize(n);iota(P.begin(),P.end(),0);int cnt=n;for(auto& x:e){int ra=find(x[0]),rb=find(x[1]);if(ra!=rb){P[ra]=rb;cnt--;}}return cnt;}
int main(){cout<<countComponents(5,{{0,1},{1,2},{3,4}})<<"\n";}
