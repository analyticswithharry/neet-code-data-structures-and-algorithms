// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 197 -- Median of Two Sorted Arrays
// Category   : Binary Search
// Difficulty : Hard
// Study Plan : Day 99
// =============================================================
//
// QUESTION:
//   Find the median of the two sorted arrays in O(log(min(m,n))).
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
double findMedianSortedArrays(vector<int> a,vector<int> b){if(a.size()>b.size())swap(a,b);int m=a.size(),n=b.size(),lo=0,hi=m;while(lo<=hi){int i=(lo+hi)/2;int j=(m+n+1)/2-i;int Lx=i>0?a[i-1]:INT_MIN,Rx=i<m?a[i]:INT_MAX,Ly=j>0?b[j-1]:INT_MIN,Ry=j<n?b[j]:INT_MAX;if(Lx<=Ry&&Ly<=Rx){if((m+n)&1)return max(Lx,Ly);return (max(Lx,Ly)+min(Rx,Ry))/2.0;}else if(Lx>Ry)hi=i-1;else lo=i+1;}return 0;}
int main(){cout<<findMedianSortedArrays({1,3},{2})<<"\n"<<findMedianSortedArrays({1,2},{3,4})<<"\n";}
