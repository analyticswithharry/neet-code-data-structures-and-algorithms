// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 090 -- Swim In Rising Water
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 45
// =============================================================
//
// QUESTION:
//   On an n x n grid, grid[i][j] is the elevation. You start at (0,0) and want to reach (n-1,n-1). At time t the water level is t and you can move to a 4-neighbor cell if both are <= t. Return the minimum t.
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
    int swimInWater(vector<vector<int>>& g){
        int n=g.size(); priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, greater<>> pq;
        pq.push({g[0][0],0,0}); vector<vector<bool>> seen(n,vector<bool>(n,false)); seen[0][0]=true; int ans=0;
        int dr[]={1,-1,0,0}, dc[]={0,0,1,-1};
        while (!pq.empty()){
            auto [v,r,c]=pq.top(); pq.pop(); ans=max(ans,v);
            if (r==n-1 && c==n-1) return ans;
            for (int k=0;k<4;k++){ int nr=r+dr[k], nc=c+dc[k];
                if (nr>=0&&nr<n&&nc>=0&&nc<n&&!seen[nr][nc]){ seen[nr][nc]=true; pq.push({g[nr][nc],nr,nc}); } }
        } return -1;
    }
};
int main(){ vector<vector<int>> g={{0,2},{1,3}}; cout<<Solution().swimInWater(g)<<endl; }
