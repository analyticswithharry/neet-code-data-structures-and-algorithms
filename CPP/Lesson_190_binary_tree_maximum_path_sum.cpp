// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 190 -- Binary Tree Maximum Path Sum
// Category   : Trees
// Difficulty : Hard
// Study Plan : Day 95
// =============================================================
//
// QUESTION:
//   Path is any sequence of nodes connected by edges (with at least one node). Return the maximum sum.
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
struct N{int v;N*l=0;N*r=0;N(int v):v(v){}};
int RES;
int dfs(N* n){if(!n)return 0;int l=max(0,dfs(n->l)),r=max(0,dfs(n->r));RES=max(RES,n->v+l+r);return n->v+max(l,r);}
int maxPathSum(N* r){RES=INT_MIN;dfs(r);return RES;}
int main(){N r(-10),a(9),b(20),c(15),d(7);r.l=&a;r.r=&b;b.l=&c;b.r=&d;cout<<maxPathSum(&r)<<"\n";}
