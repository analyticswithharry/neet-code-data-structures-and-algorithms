// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 028 -- Verifying An Alien Dictionary
// Category   : Graphs
// Difficulty : Easy
// Study Plan : Day 14
// =============================================================
//
// QUESTION:
//   In an alien language, surprisingly, they also use English lowercase
//   letters but possibly in a different order. Given a sequence of words
//   written in the alien language and the order of the alphabet, return true
//   iff the given words are sorted lexicographically in this alien language.
//
//   Example:
//     Input : words=["hello","leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"
//     Output: true
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
    bool isAlienSorted(vector<string>& words, string order) {
        int idx[26]; for (int i = 0; i < 26; ++i) idx[order[i]-'a'] = i;
        for (int w = 1; w < (int)words.size(); ++w) {
            const string& a = words[w-1]; const string& b = words[w]; bool broke = false;
            int n = min(a.size(), b.size());
            for (int i = 0; i < n; ++i) {
                int ia = idx[a[i]-'a'], ib = idx[b[i]-'a'];
                if (ia != ib) { if (ia > ib) return false; broke = true; break; }
            }
            if (!broke && a.size() > b.size()) return false;
        }
        return true;
    }
};
int main() {
    vector<string> v = {"hello","leetcode"};
    cout << boolalpha << Solution().isAlienSorted(v, "hlabcdefgijkmnopqrstuvwxyz") << endl;
}
