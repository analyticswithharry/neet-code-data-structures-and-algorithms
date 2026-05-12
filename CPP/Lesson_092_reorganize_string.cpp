// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 092 -- Reorganize String
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 46
// =============================================================
//
// QUESTION:
//   Given a string s, rearrange so no two adjacent chars are equal. Return the rearranged string, or '' if impossible.
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
    string reorganizeString(string s){
        int c[26]={0}; for (char ch: s) c[ch-'a']++;
        int n=s.size(), mx=0, idx=0;
        for (int i=0;i<26;i++) if (c[i]>mx){ mx=c[i]; idx=i; }
        if (mx > (n+1)/2) return "";
        string res(n,' '); int i=0;
        while (c[idx]>0){ res[i]='a'+idx; i+=2; c[idx]--; }
        for (int k=0;k<26;k++){
            while (c[k]>0){ if (i>=n) i=1; res[i]='a'+k; i+=2; c[k]--; }
        }
        return res;
    }
};
int main(){ cout<<Solution().reorganizeString("aab")<<" ["<<Solution().reorganizeString("aaab")<<"]"<<endl; }
