// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 099 -- Word Search
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 50
// =============================================================
//
// QUESTION:
//   Given an m x n board and a word, return true if the word exists by sequentially adjacent cells (no reuse).
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
    vector<vector<char>>* B; string W;
    bool dfs(int r,int c,int i){
        if (i==(int)W.size()) return true;
        if (r<0||r>=(int)B->size()||c<0||c>=(int)(*B)[0].size()||(*B)[r][c]!=W[i]) return false;
        char t=(*B)[r][c]; (*B)[r][c]='#';
        bool ok = dfs(r+1,c,i+1)||dfs(r-1,c,i+1)||dfs(r,c+1,i+1)||dfs(r,c-1,i+1);
        (*B)[r][c]=t; return ok;
    }
    bool exist(vector<vector<char>>& board, string word){
        B=&board; W=word;
        for (int r=0;r<(int)board.size();r++) for (int c=0;c<(int)board[0].size();c++) if (dfs(r,c,0)) return true;
        return false;
    }
};
int main(){ vector<vector<char>> b={{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
    cout<<Solution().exist(b, "ABCCED")<<endl; }
