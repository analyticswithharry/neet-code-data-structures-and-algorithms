// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 172 -- N Queens
// Category   : Backtracking
// Difficulty : Hard
// Study Plan : Day 86
// =============================================================
//
// QUESTION:
//   Place n queens on n×n board so none attack each other; return the count of distinct solutions.
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
int CNT,N; set<int> COLS,D1,D2;
void bt(int r){if(r==N){CNT++;return;}for(int c=0;c<N;c++){if(COLS.count(c)||D1.count(r-c)||D2.count(r+c))continue;COLS.insert(c);D1.insert(r-c);D2.insert(r+c);bt(r+1);COLS.erase(c);D1.erase(r-c);D2.erase(r+c);}}
int totalNQueens(int n){CNT=0;N=n;COLS.clear();D1.clear();D2.clear();bt(0);return CNT;}
int main(){cout<<totalNQueens(4)<<"\n"<<totalNQueens(6)<<"\n";}
