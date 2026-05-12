// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 175 -- Validate Binary Search Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 88
// =============================================================
//
// QUESTION:
//   Determine if a binary tree is a valid BST.
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
bool rec(N* n,long lo,long hi){if(!n)return true;if(n->v<=lo||n->v>=hi)return false;return rec(n->l,lo,n->v)&&rec(n->r,n->v,hi);}
bool isValidBST(N* r){return rec(r,LLONG_MIN,LLONG_MAX);}
int main(){N r(2),a(1),b(3);r.l=&a;r.r=&b;cout<<boolalpha<<isValidBST(&r)<<"\n";}
