// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 208 -- Maximum Frequency Stack
// Category   : Stack
// Difficulty : Hard
// Study Plan : Day 104
// =============================================================
//
// QUESTION:
//   Push/pop a stack returning the most-frequent element (ties: most recent).
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
struct FreqStack{unordered_map<int,int> f;unordered_map<int,vector<int>> g;int maxf=0;
  void push(int v){f[v]++;maxf=max(maxf,f[v]);g[f[v]].push_back(v);}
  int pop(){int v=g[maxf].back();g[maxf].pop_back();f[v]--;if(g[maxf].empty())maxf--;return v;}};
int main(){FreqStack fs;for(int x:{5,7,5,7,4,5})fs.push(x);for(int i=0;i<4;i++)cout<<fs.pop()<<" ";cout<<"\n";}
