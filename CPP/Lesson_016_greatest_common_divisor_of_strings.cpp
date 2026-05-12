// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 016 -- Greatest Common Divisor of Strings
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 8
// =============================================================
//
// QUESTION:
//   For two strings s and t, we say "t divides s" if s = t + t + ... + t.
//   Return the largest string x such that x divides both str1 and str2.
//
//   Example:
//     Input : str1="ABCABC", str2="ABC"     Output: "ABC"
//     Input : str1="ABABAB", str2="ABAB"    Output: "AB"
//     Input : str1="LEET",   str2="CODE"    Output: ""
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
    string gcdOfStrings(string s1, string s2) {
        if (s1 + s2 != s2 + s1) return "";
        return s1.substr(0, __gcd((int)s1.size(), (int)s2.size()));
    }
};
int main() {
    Solution s;
    cout << s.gcdOfStrings("ABCABC","ABC") << "|" << s.gcdOfStrings("ABABAB","ABAB") << "|" << s.gcdOfStrings("LEET","CODE") << endl;
}
