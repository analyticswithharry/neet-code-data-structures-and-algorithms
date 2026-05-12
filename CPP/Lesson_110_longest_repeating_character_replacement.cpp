// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 110 -- Longest Repeating Character Replacement
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 55
// =============================================================
//
// QUESTION:
//   Given a string s and integer k, you may change up to k characters. Return length of longest substring with all same characters.
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
    int characterReplacement(string s, int k){
        int cnt[26]={0}; int l=0, mx=0, best=0;
        for (int r=0;r<(int)s.size();r++){
            cnt[s[r]-'A']++; mx=max(mx, cnt[s[r]-'A']);
            if (r-l+1 - mx > k){ cnt[s[l]-'A']--; l++; }
            best=max(best, r-l+1);
        }
        return best;
    }
};
int main(){ Solution s; cout<<s.characterReplacement("ABAB",2)<<" "<<s.characterReplacement("AABABBA",1)<<endl; }
