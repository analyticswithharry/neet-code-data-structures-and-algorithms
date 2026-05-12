// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 181 -- Open The Lock
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 91
// =============================================================
//
// QUESTION:
//   4-wheel lock starts at '0000'. Each move turns a wheel +/-1. Avoid deadends. Return min moves to reach target or -1.
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
int openLock(vector<string> dead,string target){unordered_set<string> D(dead.begin(),dead.end());if(D.count("0000"))return -1;if(target=="0000")return 0;unordered_set<string> seen={"0000"};queue<string> q;q.push("0000");int d=0;while(!q.empty()){d++;int sz=q.size();while(sz--){string s=q.front();q.pop();for(int i=0;i<4;i++) for(int x:{-1,1}){string ns=s;ns[i]='0'+((ns[i]-'0'+x+10)%10);if(ns==target)return d;if(!seen.count(ns)&&!D.count(ns)){seen.insert(ns);q.push(ns);}}}}return -1;}
int main(){cout<<openLock({"0201","0101","0102","1212","2002"},"0202")<<"\n";}
