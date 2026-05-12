// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 053 -- Car Fleet
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 26
// =============================================================
//
// QUESTION:
//   Cars at given positions move toward target with given speeds. A car
//   that catches up forms a fleet. Return the number of fleets that arrive.
//
//   Example: target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3] -> 3
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
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int,int>> cars(n);
        for (int i=0;i<n;i++) cars[i] = {position[i], speed[i]};
        sort(cars.begin(), cars.end(), greater<>());
        vector<double> st;
        for (auto& [p,s]: cars) {
            double t = (double)(target - p) / s;
            if (st.empty() || t > st.back()) st.push_back(t);
        }
        return st.size();
    }
};
int main(){ vector<int> p={10,8,0,5,3}, s={2,4,1,1,3}; cout<<Solution().carFleet(12, p, s)<<endl; }
