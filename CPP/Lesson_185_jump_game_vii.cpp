// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 185 -- Jump Game VII
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 93
// =============================================================
//
// QUESTION:
//   Binary string s. Start at 0; can jump from i to any j with i+minJump<=j<=i+maxJump and s[j]='0'. Reach last index?
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
bool canReach(string s,int mn,int mx){int n=s.size();if(s.back()!='0'||s[0]!='0')return false;vector<int> pre(n+1,0);vector<bool> r(n,false);r[0]=true;pre[1]=1;for(int i=1;i<n;i++){if(s[i]=='0'){int lo=max(0,i-mx),hi=i-mn;if(lo<=hi && pre[hi+1]-pre[lo]>0) r[i]=true;}pre[i+1]=pre[i]+(r[i]?1:0);}return r[n-1];}
int main(){cout<<boolalpha<<canReach("011010",2,3)<<"\n"<<canReach("01101110",2,3)<<"\n";}
