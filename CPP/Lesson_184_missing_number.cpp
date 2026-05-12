// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 184 -- Missing Number
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 92
// =============================================================
//
// QUESTION:
//   Array contains n distinct numbers from [0,n]. Return the missing one.
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
int missing(vector<int> a){int x=a.size();for(int i=0;i<(int)a.size();i++)x^=i^a[i];return x;}
int main(){cout<<missing({3,0,1})<<"\n"<<missing({9,6,4,2,3,5,7,0,1})<<"\n";}
