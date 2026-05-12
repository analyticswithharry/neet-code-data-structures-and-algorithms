// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 059 -- Time Based Key Value Store
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 29
// =============================================================
//
// QUESTION:
//   Design a time-based key-value data structure that supports
//   set(key, value, timestamp) and get(key, timestamp), where get returns
//   the value with the largest timestamp <= the given timestamp.
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
class TimeMap {
    unordered_map<string, vector<pair<int,string>>> d;
public:
    void set(string k, string v, int t){ d[k].push_back({t, v}); }
    string get(string k, int t){
        if (!d.count(k)) return "";
        auto& a = d[k];
        int l=0, r=a.size()-1; string res = "";
        while (l<=r) {
            int m = (l+r)/2;
            if (a[m].first <= t) { res = a[m].second; l = m+1; } else r = m-1;
        }
        return res;
    }
};
int main(){ TimeMap tm; tm.set("foo","bar",1);
    cout<<tm.get("foo",1)<<" "<<tm.get("foo",3)<<endl;
    tm.set("foo","bar2",4);
    cout<<tm.get("foo",4)<<" "<<tm.get("foo",5)<<endl; }
