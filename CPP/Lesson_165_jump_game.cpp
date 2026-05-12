// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 165 -- Jump Game
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 83
// =============================================================
//
// QUESTION:
//   Each element is max jump length from that position. Return true iff you can reach the last index from index 0.
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
bool canJump(vector<int> a){int r=0;for(int i=0;i<(int)a.size();i++){if(i>r)return false;r=max(r,i+a[i]);}return true;}
int main(){cout<<boolalpha<<canJump({2,3,1,1,4})<<"\n"<<canJump({3,2,1,0,4})<<"\n";}
