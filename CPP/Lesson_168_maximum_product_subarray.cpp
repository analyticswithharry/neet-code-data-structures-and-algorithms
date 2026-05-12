// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 168 -- Maximum Product Subarray
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 84
// =============================================================
//
// QUESTION:
//   Find a contiguous subarray with the largest product.
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
int maxProduct(vector<int> a){int mx=a[0],mn=a[0],res=a[0];for(int i=1;i<(int)a.size();i++){int v=a[i];if(v<0)swap(mx,mn);mx=max(v,mx*v);mn=min(v,mn*v);res=max(res,mx);}return res;}
int main(){cout<<maxProduct({2,3,-2,4})<<"\n"<<maxProduct({-2,0,-1})<<"\n";}
