// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 089 -- Reconstruct Itinerary
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 45
// =============================================================
//
// QUESTION:
//   Given a list of airline tickets [from,to], reconstruct the itinerary in order, starting from 'JFK'. If multiple valid, return the lexicographically smallest one.
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
    vector<string> findItinerary(vector<vector<string>>& tickets){
        map<string, multiset<string>> g;
        for (auto& t: tickets) g[t[0]].insert(t[1]);
        vector<string> st={"JFK"}, res;
        while (!st.empty()){
            while (g.count(st.back()) && !g[st.back()].empty()){
                auto it = g[st.back()].begin(); string nxt = *it; g[st.back()].erase(it); st.push_back(nxt);
            }
            res.push_back(st.back()); st.pop_back();
        }
        reverse(res.begin(), res.end()); return res;
    }
};
int main(){ vector<vector<string>> t={{"MUC","LHR"},{"JFK","MUC"},{"SFO","SJC"},{"LHR","SFO"}};
    for (auto& s: Solution().findItinerary(t)) cout<<s<<" "; cout<<endl; }
