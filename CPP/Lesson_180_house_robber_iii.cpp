// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 180 -- House Robber III
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 90
// =============================================================
//
// QUESTION:
//   Houses arranged as a binary tree; cannot rob two directly-linked houses. Return max amount.
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
pair<int,int> rec(N* n){if(!n)return {0,0};auto l=rec(n->l);auto r=rec(n->r);return {n->v+l.second+r.second,max(l.first,l.second)+max(r.first,r.second)};}
int rob(N* r){auto x=rec(r);return max(x.first,x.second);}
int main(){N r(3),a(2),b(3),c(3),d(1);r.l=&a;a.r=&b;r.r=&c;c.r=&d;cout<<rob(&r)<<"\n";}
