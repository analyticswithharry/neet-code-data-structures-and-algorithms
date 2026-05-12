// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 161 -- Pow x n
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 81
// =============================================================
//
// QUESTION:
//   Implement pow(x, n) — x raised to the n-th power.
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
double myPow(double x,long long n){if(n<0){x=1/x;n=-n;}double r=1.0;while(n){if(n&1)r*=x;x*=x;n>>=1;}return r;}
int main(){cout<<myPow(2.0,10)<<"\n"<<myPow(2.0,-2)<<"\n";}
