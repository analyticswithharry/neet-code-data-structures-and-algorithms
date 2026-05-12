// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 192 -- Word Break II
// Category   : Backtracking
// Difficulty : Hard
// Study Plan : Day 96
// =============================================================
//
// QUESTION:
//   Return all sentences obtainable by segmenting s using words from dict.
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
unordered_map<int,vector<string>> M; string S; unordered_set<string> W;
vector<string> dfs(int i){if(i==(int)S.size())return {""};if(M.count(i))return M[i];vector<string> out;for(int j=i+1;j<=(int)S.size();j++){string p=S.substr(i,j-i);if(W.count(p))for(auto& t:dfs(j))out.push_back(p+(t.empty()?"":" "+t));}return M[i]=out;}
vector<string> wordBreak(string s,vector<string> wd){M.clear();S=s;W=unordered_set<string>(wd.begin(),wd.end());return dfs(0);}
int main(){auto r=wordBreak("catsanddog",{"cat","cats","and","sand","dog"});for(auto& s:r)cout<<s<<"\n";}
