// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 195 -- Boats to Save People
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 98
// =============================================================
//
// QUESTION:
//   Each boat holds at most 2 people, total weight <= limit. Return min boats.
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
int numRescueBoats(vector<int> p,int limit){sort(p.begin(),p.end());int i=0,j=p.size()-1,b=0;while(i<=j){if(p[i]+p[j]<=limit)i++;j--;b++;}return b;}
int main(){cout<<numRescueBoats({3,2,2,1},3)<<"\n"<<numRescueBoats({3,5,3,4},5)<<"\n";}
