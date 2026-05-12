// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 108 -- Evaluate Reverse Polish Notation
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 54
// =============================================================
//
// QUESTION:
//   Evaluate an arithmetic expression in Reverse Polish Notation. Operators: +, -, *, /. Division truncates toward zero.
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
    int evalRPN(vector<string>& tokens){
        stack<long long> st;
        for (auto& t: tokens){
            if (t.size()==1 && string("+-*/").find(t[0])!=string::npos){
                long long b=st.top(); st.pop(); long long a=st.top(); st.pop();
                if (t=="+") st.push(a+b);
                else if (t=="-") st.push(a-b);
                else if (t=="*") st.push(a*b);
                else st.push(a/b);
            } else st.push(stoll(t));
        }
        return (int)st.top();
    }
};
int main(){ vector<string> a={"2","1","+","3","*"}, b={"10","6","9","3","+","-11","*","/","*","17","+","5","+"};
    cout<<Solution().evalRPN(a)<<" "<<Solution().evalRPN(b)<<endl; }
