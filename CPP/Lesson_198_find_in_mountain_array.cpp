// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 198 -- Find in Mountain Array
// Category   : Binary Search
// Difficulty : Hard
// Study Plan : Day 99
// =============================================================
//
// QUESTION:
//   Mountain array: strictly increasing then strictly decreasing. Return min index with value=target.
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
int bs(vector<int>& a,int l,int r,int t,bool asc){while(l<=r){int m=(l+r)/2;if(a[m]==t)return m;if(asc){if(a[m]<t)l=m+1;else r=m-1;}else{if(a[m]>t)l=m+1;else r=m-1;}}return -1;}
int findInMountainArray(int t,vector<int> a){int lo=0,hi=a.size()-1;while(lo<hi){int m=(lo+hi)/2;if(a[m]<a[m+1])lo=m+1;else hi=m;}int p=lo;int i=bs(a,0,p,t,true);return i!=-1?i:bs(a,p+1,a.size()-1,t,false);}
int main(){cout<<findInMountainArray(3,{1,2,3,4,5,3,1})<<"\n";}
