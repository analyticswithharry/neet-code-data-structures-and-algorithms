// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 102 -- Longest Common Subsequence
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 51
// =============================================================
//
// QUESTION:
//   Given two strings text1 and text2, return the length of their longest common subsequence.
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
    int longestCommonSubsequence(string a, string b){
        int m=a.size(), n=b.size();
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        for (int i=0;i<m;i++) for (int j=0;j<n;j++){
            if (a[i]==b[j]) dp[i+1][j+1]=dp[i][j]+1;
            else dp[i+1][j+1]=max(dp[i][j+1], dp[i+1][j]);
        }
        return dp[m][n];
    }
};
int main(){ cout<<Solution().longestCommonSubsequence("abcde","ace")<<endl; }
