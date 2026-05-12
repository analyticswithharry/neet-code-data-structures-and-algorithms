// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 209 -- Hand of Straights
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 105
// =============================================================
//
// QUESTION:
//   Can hand be rearranged into groups of size W of consecutive cards?
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
bool isNStraightHand(vector<int> h,int W){if((int)h.size()%W)return false;map<int,int> c;for(int x:h)c[x]++;for(auto& p:c){if(p.second>0){int cnt=p.second;for(int k=0;k<W;k++){if(c[p.first+k]<cnt)return false;c[p.first+k]-=cnt;}}}return true;}
int main(){cout<<boolalpha<<isNStraightHand({1,2,3,6,2,3,4,7,8},3)<<"\n"<<isNStraightHand({1,2,3,4,5},4)<<"\n";}
