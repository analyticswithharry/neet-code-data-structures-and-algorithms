// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 162 -- Multiply Strings
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 81
// =============================================================
//
// QUESTION:
//   Given two non-negative integers as strings, return their product as a string. Do not use built-in big-int conversion.
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
string mul(string a,string b){if(a=="0"||b=="0")return "0";int n=a.size(),m=b.size();vector<int> r(n+m,0);for(int i=n-1;i>=0;i--)for(int j=m-1;j>=0;j--){int p=(a[i]-'0')*(b[j]-'0');int s=p+r[i+j+1];r[i+j+1]=s%10;r[i+j]+=s/10;}string out;for(int v:r)out+=char('0'+v);size_t k=out.find_first_not_of('0');return k==string::npos?"0":out.substr(k);}
int main(){cout<<mul("123","456")<<"\n";}
