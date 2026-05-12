// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 186 -- Gas Station
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 93
// =============================================================
//
// QUESTION:
//   Gas[i]/cost[i] arrays around a circular route. Return start index to complete the circuit (or -1).
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
int canCompleteCircuit(vector<int> g,vector<int> c){int s=0,t=0,tot=0;for(int i=0;i<(int)g.size();i++){int d=g[i]-c[i];t+=d;tot+=d;if(t<0){s=i+1;t=0;}}return tot<0?-1:s;}
int main(){cout<<canCompleteCircuit({1,2,3,4,5},{3,4,5,1,2})<<"\n"<<canCompleteCircuit({2,3,4},{3,4,3})<<"\n";}
