// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 171 -- Partition to K Equal Sum Subsets
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 86
// =============================================================
//
// QUESTION:
//   Determine if nums can be partitioned into k subsets with equal sum.
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
int t,K; vector<int> N,B;
bool bt(int i){if(i==(int)N.size())return true;for(int j=0;j<K;j++){if(B[j]+N[i]<=t){B[j]+=N[i];if(bt(i+1))return true;B[j]-=N[i];}if(B[j]==0)break;}return false;}
bool canPartitionKSubsets(vector<int> nums,int k){int s=0;for(int v:nums)s+=v;if(s%k)return false;t=s/k;sort(nums.begin(),nums.end(),greater<>());if(nums[0]>t)return false;K=k;N=nums;B.assign(k,0);return bt(0);}
int main(){cout<<boolalpha<<canPartitionKSubsets({4,3,2,3,5,2,1},4)<<"\n";}
