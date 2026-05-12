// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 189 -- Delete Leaves With a Given Value
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 95
// =============================================================
//
// QUESTION:
//   Delete all leaf nodes with a given target value (cascade).
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
N* rem(N* n,int t){if(!n)return 0;n->l=rem(n->l,t);n->r=rem(n->r,t);if(!n->l&&!n->r&&n->v==t)return 0;return n;}
void show(N* n){if(!n){cout<<"null";return;}cout<<"["<<n->v<<",";show(n->l);cout<<",";show(n->r);cout<<"]";}
int main(){N r(1),a(2),b(2),c(3),d(2),e(4);r.l=&a;a.l=&b;r.r=&c;c.l=&d;c.r=&e;show(rem(&r,2));cout<<"\n";}
