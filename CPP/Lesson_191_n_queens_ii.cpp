// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 191 -- N Queens II
// Category   : Backtracking
// Difficulty : Hard
// Study Plan : Day 96
// =============================================================
//
// QUESTION:
//   Return number of distinct solutions for n-queens.
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
int CNT,N; set<int> C,D1,D2;
void bt(int r){if(r==N){CNT++;return;}for(int i=0;i<N;i++){if(C.count(i)||D1.count(r-i)||D2.count(r+i))continue;C.insert(i);D1.insert(r-i);D2.insert(r+i);bt(r+1);C.erase(i);D1.erase(r-i);D2.erase(r+i);}}
int totalNQueens(int n){CNT=0;N=n;C.clear();D1.clear();D2.clear();bt(0);return CNT;}
int main(){cout<<totalNQueens(4)<<"\n"<<totalNQueens(8)<<"\n";}
