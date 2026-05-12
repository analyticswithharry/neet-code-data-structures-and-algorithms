// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 035 -- Sum of All Subsets XOR Total
// Category   : Backtracking
// Difficulty : Easy
// Study Plan : Day 18
// =============================================================
//
// QUESTION:
//   The XOR total of an array is the bitwise XOR of all its elements (or 0
//   if empty). Return the sum of all XOR totals for every subset of nums.
//
//   Example:
//     Input : [1,3]      Output: 6   (subsets: [],[1],[3],[1,3] -> 0+1+3+2 = 6)
//     Input : [5,1,6]    Output: 28
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
    int total;
    void dfs(vector<int>& a, int i, int cur) {
        if (i == (int)a.size()) { total += cur; return; }
        dfs(a, i+1, cur); dfs(a, i+1, cur ^ a[i]);
    }
public:
    int subsetXORSum(vector<int>& nums) { total = 0; dfs(nums, 0, 0); return total; }
};
int main() {
    Solution s;
    vector<int> a = {1,3}, b = {5,1,6};
    cout << s.subsetXORSum(a) << " " << s.subsetXORSum(b) << endl;
}
