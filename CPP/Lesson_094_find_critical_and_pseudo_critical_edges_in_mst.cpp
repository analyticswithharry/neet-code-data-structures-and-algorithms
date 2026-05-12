// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 094 -- Find Critical and Pseudo Critical Edges in MST
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 47
// =============================================================
//
// QUESTION:
//   Given n nodes and weighted edges, find indices of critical and pseudo-critical edges in any MST.
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
struct DSU { vector<int> p,r; int cnt;
    DSU(int n):p(n),r(n,0),cnt(n){ iota(p.begin(),p.end(),0); }
    int f(int x){ while(p[x]!=x){ p[x]=p[p[x]]; x=p[x]; } return x; }
    bool u(int a,int b){ a=f(a); b=f(b); if(a==b) return false;
        if(r[a]<r[b]) swap(a,b); p[b]=a; if(r[a]==r[b]) r[a]++; cnt--; return true; }
};
class Solution { public:
    int n; vector<vector<int>> E;
    int kruskal(int skip, int force){
        DSU d(n); int w=0;
        if (force>=0){ if(!d.u(E[force][0],E[force][1])) return INT_MAX; w+=E[force][2]; }
        for (int i=0;i<(int)E.size();i++){ if(i==skip) continue; if(d.u(E[i][0],E[i][1])) w+=E[i][2]; }
        return d.cnt==1 ? w : INT_MAX;
    }
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int N, vector<vector<int>>& edges){
        n=N; E=edges; for (int i=0;i<(int)E.size();i++) E[i].push_back(i);
        sort(E.begin(),E.end(),[](auto&a,auto&b){return a[2]<b[2];});
        int base=kruskal(-1,-1); vector<int> crit, pseu;
        for (int i=0;i<(int)E.size();i++){
            if (kruskal(i,-1) > base) crit.push_back(E[i][3]);
            else if (kruskal(-1,i) == base) pseu.push_back(E[i][3]);
        }
        return {crit, pseu};
    }
};
int main(){ vector<vector<int>> e={{0,1,1},{1,2,1},{2,3,2},{0,3,2},{0,4,3},{3,4,3},{1,4,6}};
    auto r=Solution().findCriticalAndPseudoCriticalEdges(5,e);
    for (auto& v: r){ cout<<"["; for(int x: v)cout<<x<<","; cout<<"] "; } cout<<endl; }
