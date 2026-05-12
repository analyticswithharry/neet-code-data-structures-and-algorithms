// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 047 -- Longest Repeating Character Replacement
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 23
// =============================================================
//
// QUESTION:
//   Given a string s and integer k, you can change at most k characters.
//   Return length of the longest substring with all same characters.
//
//   Example: s="AABABBA", k=1 -> 4
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
    int characterReplacement(string s, int k) {
        int cnt[26] = {0}; int l=0, best=0, mf=0;
        for (int r=0;r<(int)s.size();r++) {
            cnt[s[r]-'A']++;
            mf = max(mf, cnt[s[r]-'A']);
            if (r - l + 1 - mf > k) { cnt[s[l]-'A']--; l++; }
            best = max(best, r - l + 1);
        }
        return best;
    }
};
int main(){ cout<<Solution().characterReplacement("AABABBA", 1)<<endl; }
