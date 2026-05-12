// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 050 -- Evaluate Reverse Polish Notation
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 25
// =============================================================
//
// QUESTION:
//   Evaluate an arithmetic expression in Reverse Polish Notation.
//
//   Example: ["2","1","+","3","*"] -> 9
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
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        for (auto& t: tokens) {
            if (t=="+"||t=="-"||t=="*"||t=="/") {
                int b = st.top(); st.pop(); int a = st.top(); st.pop();
                if (t=="+") st.push(a+b);
                else if (t=="-") st.push(a-b);
                else if (t=="*") st.push(a*b);
                else st.push(a/b);
            } else st.push(stoi(t));
        }
        return st.top();
    }
};
int main(){ vector<string> v={"2","1","+","3","*"}; cout<<Solution().evalRPN(v)<<endl; }
