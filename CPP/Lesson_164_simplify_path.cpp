// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 164 -- Simplify Path
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 82
// =============================================================
//
// QUESTION:
//   Given a Unix-style absolute path, return the simplified canonical path.
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
string simplify(string p){vector<string> st;string cur;stringstream ss(p);string part;while(getline(ss,part,'/')){if(part==""||part==".")continue;if(part==".."){if(!st.empty())st.pop_back();}else st.push_back(part);}string out;for(auto& s:st) out+="/"+s;return out.empty()?"/":out;}
int main(){cout<<simplify("/a/./b/../../c/")<<"\n"<<simplify("/home//foo/")<<"\n";}
