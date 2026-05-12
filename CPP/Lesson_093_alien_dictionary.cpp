// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 093 -- Alien Dictionary
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 47
// =============================================================
//
// QUESTION:
//   Given a sorted list of words from an alien language, derive the order of letters. Return any valid order or '' if impossible.
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
class Solution { public:
    string alienOrder(vector<string>& words){
        unordered_map<char, unordered_set<char>> g;
        unordered_map<char,int> ind;
        for (auto& w: words) for (char c: w){ g[c]; if (!ind.count(c)) ind[c]=0; }
        for (int i=0;i+1<(int)words.size();i++){
            auto& a=words[i]; auto& b=words[i+1]; bool found=false;
            int m=min(a.size(),b.size());
            for (int j=0;j<m;j++){
                if (a[j]!=b[j]){ if (g[a[j]].insert(b[j]).second) ind[b[j]]++; found=true; break; }
            }
            if (!found && a.size()>b.size()) return "";
        }
        queue<char> q; for (auto& p: ind) if (p.second==0) q.push(p.first);
        string res;
        while (!q.empty()){
            char c=q.front(); q.pop(); res+=c;
            for (char nx: g[c]) if (--ind[nx]==0) q.push(nx);
        }
        return res.size()==ind.size() ? res : "";
    }
};
int main(){ vector<string> w={"wrt","wrf","er","ett","rftt"}; cout<<Solution().alienOrder(w)<<endl; }
