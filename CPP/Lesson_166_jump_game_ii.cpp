// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 166 -- Jump Game II
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 83
// =============================================================
//
// QUESTION:
//   Return the minimum number of jumps to reach the last index. Assume reachable.
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
int jump(vector<int> a){int j=0,cur=0,far=0;for(int i=0;i<(int)a.size()-1;i++){far=max(far,i+a[i]);if(i==cur){j++;cur=far;}}return j;}
int main(){cout<<jump({2,3,1,1,4})<<"\n"<<jump({2,3,0,1,4})<<"\n";}
