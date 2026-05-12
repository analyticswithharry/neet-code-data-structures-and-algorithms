// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 187 -- Reverse Linked List II
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 94
// =============================================================
//
// QUESTION:
//   Reverse the nodes of the list from position left to right (1-indexed).
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
struct N{int v;N* n=0;N(int v):v(v){}};
N* reverseBetween(N* h,int L,int R){N d(0);d.n=h;N* pre=&d;for(int i=0;i<L-1;i++)pre=pre->n;N* cur=pre->n;for(int i=0;i<R-L;i++){N* nxt=cur->n;cur->n=nxt->n;nxt->n=pre->n;pre->n=nxt;}return d.n;}
int main(){N* h=new N(1);N* c=h;for(int v:{2,3,4,5}){c->n=new N(v);c=c->n;}N* r=reverseBetween(h,2,4);while(r){cout<<r->v<<" ";r=r->n;}cout<<"\n";}
