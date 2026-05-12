// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 015 -- Excel Sheet Column Title
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 8
// =============================================================
//
// QUESTION:
//   Given an integer columnNumber, return its corresponding column title
//   as it appears in an Excel sheet.
//
//   Example:
//     1  -> A
//     28 -> AB
//     701 -> ZY
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
    string convertToTitle(int n) {
        string out;
        while (n > 0) { --n; out += char('A' + n % 26); n /= 26; }
        reverse(out.begin(), out.end());
        return out;
    }
};
int main() {
    Solution s;
    cout << s.convertToTitle(1) << " " << s.convertToTitle(28) << " " << s.convertToTitle(701) << endl;
}
