// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 207 -- Decode String
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 104
// =============================================================
//
// QUESTION:
//   Decode a run-length-style string like "3[a2[c]]" -> "accaccacc".
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
string decodeString(string s){vector<pair<string,int>> st;string cur;int k=0;for(char ch:s){if(isdigit(ch))k=k*10+(ch-'0');else if(ch=='['){st.push_back({cur,k});cur="";k=0;}else if(ch==']'){auto [pre,n]=st.back();st.pop_back();string nb=pre;for(int i=0;i<n;i++)nb+=cur;cur=nb;}else cur+=ch;}return cur;}
int main(){cout<<decodeString("3[a]2[bc]")<<"\n"<<decodeString("3[a2[c]]")<<"\n";}
