// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 049 -- Min Stack
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 24
// =============================================================
//
// QUESTION:
//   Design a stack supporting push, pop, top, and getMin in O(1).
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
class MinStack {
    stack<int> s, m;
public:
    void push(int v){ s.push(v); m.push(m.empty()?v:min(v,m.top())); }
    void pop(){ s.pop(); m.pop(); }
    int top(){ return s.top(); }
    int getMin(){ return m.top(); }
};
int main(){ MinStack s; s.push(-2); s.push(0); s.push(-3); cout<<s.getMin()<<" "; s.pop(); cout<<s.top()<<" "<<s.getMin()<<endl; }
