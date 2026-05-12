// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 100 -- Palindrome Partitioning
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 50
// =============================================================
//
// QUESTION:
//   Partition string s such that every substring is a palindrome. Return all possible partitions.
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
    vector<vector<string>> res; vector<string> cur;
    bool isPal(const string& s){ for (int i=0,j=s.size()-1;i<j;i++,j--) if (s[i]!=s[j]) return false; return true; }
    void bt(const string& s, int i){
        if (i==(int)s.size()){ res.push_back(cur); return; }
        for (int j=i+1;j<=(int)s.size();j++){
            string sub = s.substr(i, j-i);
            if (isPal(sub)){ cur.push_back(sub); bt(s, j); cur.pop_back(); }
        }
    }
    vector<vector<string>> partition(string s){ bt(s, 0); return res; }
};
int main(){ for (auto& v: Solution().partition("aab")){ cout<<"["; for (auto& x: v) cout<<x<<","; cout<<"] "; } cout<<endl; }
