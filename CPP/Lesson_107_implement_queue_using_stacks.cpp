// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 107 -- Implement Queue using Stacks
// Category   : Stack
// Difficulty : Easy
// Study Plan : Day 54
// =============================================================
//
// QUESTION:
//   Implement a FIFO queue using only two stacks.
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
class MyQueue {
    stack<int> a, b;
public:
    void push(int x){ a.push(x); }
    int pop(){ peek(); int t=b.top(); b.pop(); return t; }
    int peek(){ if (b.empty()) while (!a.empty()){ b.push(a.top()); a.pop(); } return b.top(); }
    bool empty(){ return a.empty() && b.empty(); }
};
int main(){ MyQueue q; q.push(1); q.push(2);
    cout<<q.peek()<<" "<<q.pop()<<" "<<q.empty()<<endl; }
