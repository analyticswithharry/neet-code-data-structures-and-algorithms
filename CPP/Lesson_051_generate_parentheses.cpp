// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 051 -- Generate Parentheses
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 25
// =============================================================
//
// QUESTION:
//   Given n, return all valid combinations of n pairs of parentheses.
//
//   Example: n=3 -> ["((()))","(()())","(())()","()(())","()()()"]
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
class Solution {
    void bt(vector<string>& r, string cur, int o, int c, int n) {
        if ((int)cur.size()==2*n) { r.push_back(cur); return; }
        if (o<n) bt(r, cur+"(", o+1, c, n);
        if (c<o) bt(r, cur+")", o, c+1, n);
    }
public:
    vector<string> generateParenthesis(int n) {
        vector<string> r; bt(r, "", 0, 0, n); return r;
    }
};
int main(){ for (auto& s: Solution().generateParenthesis(3)) cout<<s<<" "; cout<<endl; }
