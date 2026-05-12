// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 022 -- Valid Parentheses
// Category   : Stack
// Difficulty : Easy
// Study Plan : Day 11
// =============================================================
//
// QUESTION:
//   Given a string s containing just the characters '(', ')', '{', '}',
//   '[' and ']', determine if the input string is valid. An input string is
//   valid if open brackets are closed by the same type of brackets in the
//   correct order.
//
//   Example:
//     Input : "()[]{}"   Output: true
//     Input : "(]"       Output: false
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
    bool isValid(string s) {
        unordered_map<char,char> m = {{')','('}, {']','['}, {'}','{'}};
        stack<char> st;
        for (char c : s) {
            if (m.count(c)) { if (st.empty() || st.top() != m[c]) return false; st.pop(); }
            else st.push(c);
        }
        return st.empty();
    }
};
int main() {
    Solution s;
    cout << boolalpha << s.isValid("()[]{}") << " " << s.isValid("(]") << endl;
}
