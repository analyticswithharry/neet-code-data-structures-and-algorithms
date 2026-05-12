// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 091 -- Single Threaded CPU
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 46
// =============================================================
//
// QUESTION:
//   You have tasks[i] = [enqueueTime, processingTime]. CPU picks the task with shortest processing time available; ties broken by index. Return order of indices.
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
    vector<int> getOrder(vector<vector<int>>& tasks){
        int n=tasks.size(); vector<int> idx(n); iota(idx.begin(),idx.end(),0);
        sort(idx.begin(),idx.end(), [&](int a,int b){return tasks[a][0]<tasks[b][0];});
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
        long long t=0; int i=0; vector<int> res;
        while (i<n || !pq.empty()){
            if (pq.empty()) t=max(t, (long long)tasks[idx[i]][0]);
            while (i<n && tasks[idx[i]][0]<=t){ pq.push({tasks[idx[i]][1], idx[i]}); i++; }
            auto [p,j]=pq.top(); pq.pop(); t+=p; res.push_back(j);
        }
        return res;
    }
};
int main(){ vector<vector<int>> t={{1,2},{2,4},{3,2},{4,1}};
    for (int x: Solution().getOrder(t)) cout<<x<<" "; cout<<endl; }
