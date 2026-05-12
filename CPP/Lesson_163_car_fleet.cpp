// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 163 -- Car Fleet
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 82
// =============================================================
//
// QUESTION:
//   Cars at positions head to target with given speeds. Cars cannot pass; slower car ahead caps faster car behind. Return number of fleets that arrive.
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
int carFleet(int target,vector<int> pos,vector<int> sp){int n=pos.size();vector<pair<int,int>> c;for(int i=0;i<n;i++)c.push_back({pos[i],sp[i]});sort(c.begin(),c.end(),greater<>());int f=0;double lt=0;for(auto& p:c){double t=(double)(target-p.first)/p.second;if(t>lt){f++;lt=t;}}return f;}
int main(){cout<<carFleet(12,{10,8,0,5,3},{2,4,1,1,3})<<"\n";}
