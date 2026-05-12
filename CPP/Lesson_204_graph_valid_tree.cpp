// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 204 -- Graph Valid Tree
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 102
// =============================================================
//
// QUESTION:
//   Given n nodes and edges, determine if they form a tree (connected and no cycles).
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
bool validTree(int n,vector<vector<int>> e){if((int)e.size()!=n-1)return false;P.resize(n);iota(P.begin(),P.end(),0);for(auto& x:e){int ra=find(x[0]),rb=find(x[1]);if(ra==rb)return false;P[ra]=rb;}return true;}
int main(){cout<<boolalpha<<validTree(5,{{0,1},{0,2},{0,3},{1,4}})<<"\n"<<validTree(5,{{0,1},{1,2},{2,3},{1,3},{1,4}})<<"\n";}
