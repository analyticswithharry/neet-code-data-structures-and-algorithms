// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 023 -- Extra Characters in a String
// Category   : Tries
// Difficulty : Medium
// Study Plan : Day 12
// =============================================================
//
// QUESTION:
//   Given a string s and a dictionary of words, break s into one or more
//   non-overlapping substrings such that each substring is in dictionary.
//   There may be characters in s that are not in any of the substrings.
//   Return the minimum number of extra characters left over.
//
//   Example:
//     Input : s = "leetscode", dict = ["leet","code","leetcode"]
//     Output: 1   (the 's' is extra)
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
    int minExtraChar(string s, vector<string>& dictionary) {
        unordered_set<string> words(dictionary.begin(), dictionary.end());
        int n = s.size(); vector<int> dp(n+1, 0);
        for (int i = 1; i <= n; ++i) {
            dp[i] = dp[i-1] + 1;
            for (int j = 0; j < i; ++j)
                if (words.count(s.substr(j, i-j))) dp[i] = min(dp[i], dp[j]);
        }
        return dp[n];
    }
};
int main() {
    vector<string> d = {"leet","code","leetcode"};
    cout << Solution().minExtraChar("leetscode", d) << endl;
}
