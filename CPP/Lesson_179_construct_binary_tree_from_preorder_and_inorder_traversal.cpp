// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 179 -- Construct Binary Tree From Preorder And Inorder Traversal
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 90
// =============================================================
//
// QUESTION:
//   Given preorder and inorder traversals (no duplicates), reconstruct the binary tree.
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
int P; vector<int> PRE; unordered_map<int,int> IDX;
N* rec(int lo,int hi){if(lo>hi)return 0;int v=PRE[P++];int k=IDX[v];N* n=new N(v);n->l=rec(lo,k-1);n->r=rec(k+1,hi);return n;}
N* build(vector<int> pre,vector<int> ino){P=0;PRE=pre;IDX.clear();for(int i=0;i<(int)ino.size();i++)IDX[ino[i]]=i;return rec(0,ino.size()-1);}
void pre_order(N* n,vector<int>& r){if(!n)return;r.push_back(n->v);pre_order(n->l,r);pre_order(n->r,r);}
int main(){auto t=build({3,9,20,15,7},{9,3,15,20,7});vector<int> r;pre_order(t,r);for(int x:r)cout<<x<<" ";cout<<"\n";}
