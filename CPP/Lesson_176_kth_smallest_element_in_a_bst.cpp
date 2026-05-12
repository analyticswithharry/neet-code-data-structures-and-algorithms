// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 176 -- Kth Smallest Element In a Bst
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 88
// =============================================================
//
// QUESTION:
//   Return the kth smallest value in a BST (1-indexed).
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
int kth(N* r,int k){stack<N*> st;N* cur=r;while(cur||!st.empty()){while(cur){st.push(cur);cur=cur->l;}cur=st.top();st.pop();if(--k==0)return cur->v;cur=cur->r;}return -1;}
int main(){N r(3),a(1),b(2),c(4);r.l=&a;a.r=&b;r.r=&c;cout<<kth(&r,1)<<"\n"<<kth(&r,3)<<"\n";}
