// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 210 -- Dota2 Senate
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 105
// =============================================================
//
// QUESTION:
//   Senate string of 'R'/'D'. Each round senators ban earliest opponent. Return winning party.
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
string predictPartyVictory(string s){queue<int> R,D;int n=s.size();for(int i=0;i<n;i++) (s[i]=='R'?R:D).push(i);while(!R.empty()&&!D.empty()){int r=R.front();R.pop();int d=D.front();D.pop();if(r<d)R.push(r+n);else D.push(d+n);}return R.empty()?"Dire":"Radiant";}
int main(){cout<<predictPartyVictory("RD")<<"\n"<<predictPartyVictory("RDD")<<"\n";}
