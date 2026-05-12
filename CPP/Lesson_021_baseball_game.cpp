// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 021 -- Baseball Game
// Category   : Stack
// Difficulty : Easy
// Study Plan : Day 11
// =============================================================
//
// QUESTION:
//   You are keeping the scores for a baseball game. Operations:
//     Integer x : record a new score x
//     '+'       : record sum of previous two scores
//     'D'       : record double of previous score
//     'C'       : invalidate the previous score, removing it
//   Return the sum of all the scores after all operations.
//
//   Example:
//     Input : ops = ["5","2","C","D","+"]
//     Output: 30   (records: 5, 10, 15)
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
    int calPoints(vector<string>& ops) {
        vector<int> st;
        for (auto& o : ops) {
            if (o == "+") st.push_back(st[st.size()-1] + st[st.size()-2]);
            else if (o == "D") st.push_back(2 * st.back());
            else if (o == "C") st.pop_back();
            else st.push_back(stoi(o));
        }
        return accumulate(st.begin(), st.end(), 0);
    }
};
int main() {
    vector<string> v = {"5","2","C","D","+"};
    cout << Solution().calPoints(v) << endl;
}
